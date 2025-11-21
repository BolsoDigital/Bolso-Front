import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Expenses
from .forms import ExpenseForm
from django.db.models import Sum, Avg
from django.utils import timezone
from datetime import timedelta


@login_required(login_url='login')
def expenses_list(request):
    expenses = Expenses.objects.filter(id_user=request.user.id)
    return render(request, 'expenses_list.html', {'expenses': expenses})


@login_required(login_url='login')
def upload_payment(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            response = requests.post(
                "http://localhost:8000/ai/upload-payment/",
                data={'id_user': request.user.id},
                files={'image': (file.name, file.read(), file.content_type)}
            )
            if response.status_code == 200:
                messages.success(request, "Comprovante enviado com sucesso!")
            else:
                messages.error(request, f"Erro ao enviar: {response.text}")
        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
    return redirect('bolsoDigital:expenses_list')


@login_required(login_url='login')
def delete_payment(request, expense_id):
    try:
        response = requests.delete(
            f"http://localhost:8000/ai/delete-payment/{expense_id}?id_user={request.user.id}"
        )
        if response.status_code == 200:
            messages.success(request, f"Pagamento {expense_id} deletado com sucesso!")
        elif response.status_code == 404:
            messages.error(request, f"Pagamento {expense_id} não encontrado.")
        else:
            messages.error(request, f"Erro ao deletar: {response.text}")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro: {e}")

    return redirect('bolsoDigital:expenses_list')

@login_required(login_url='login')
def edit_payment(request, id):
    expense = get_object_or_404(Expenses, pk=id)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.id_user = request.user
            print("Usuário:", expense.id_user)
            print("Categoria:", expense.id_category)            
            expense.save()
            messages.success(request, "Pagamento atualizado com sucesso!")
            return redirect('bolsoDigital:expenses_list')
        else:
            messages.error(request, f"Erro ao salvar: {form.errors}")
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'edit_payment.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    # Pega todos os gastos do usuário logado
    user_expenses = Expenses.objects.filter(id_user=request.user)
    
    # --- 1. Cálculos dos "Cards" ---
    
    # Total gasto (geral)
    total_spent_data = user_expenses.aggregate(total=Sum('value'))
    total_spent = total_spent_data['total'] or 0
    
    # Total gasto nos últimos 30 dias
    thirty_days_ago = timezone.now() - timedelta(days=30)
    recent_spent_data = user_expenses.filter(update_at__gte=thirty_days_ago).aggregate(total=Sum('value'))
    recent_spent = recent_spent_data['total'] or 0
    
    # Valor médio por transação
    average_spent_data = user_expenses.aggregate(avg=Avg('value'))
    average_spent = average_spent_data['avg'] or 0
    
    # Número de transações
    transaction_count = user_expenses.count()
    
    
    # --- 2. Dados para o Gráfico de Categoria ---
    
    # Agrupa os gastos por nome da categoria e soma os valores
    spending_by_category = user_expenses.values('id_category__name') \
                                        .annotate(total=Sum('value')) \
                                        .order_by('-total')
    
    # Prepara os dados para o Chart.js
    # (Converte Decimals para floats para o JavaScript)
    chart_labels = [item['id_category__name'] for item in spending_by_category]
    chart_data = [float(item['total']) for item in spending_by_category]
    
    
    # --- 3. Lista de Transações Recentes ---
    recent_transactions = user_expenses.order_by('-update_at')[:5]

    
    # --- 4. Envia tudo para o template ---
    context = {
        'total_spent': total_spent,
        'recent_spent': recent_spent,
        'average_spent': average_spent,
        'transaction_count': transaction_count,
        'recent_transactions': recent_transactions,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }
    
    return render(request, 'dashboard.html', context)
