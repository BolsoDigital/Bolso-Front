import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Expenses

def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', {'expenses': expenses})

def upload_payment(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            response = requests.post(
                "http://localhost:8000/ai/upload-payment/",
                files={'image': (file.name, file.read(), file.content_type)}
            )
            if response.status_code == 200:
                messages.success(request, "Comprovante enviado com sucesso!")
            else:
                messages.error(request, f"Erro ao enviar: {response.text}")
        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
    return redirect('bolsoDigital:expenses_list')


def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', {'expenses': expenses})

def delete_payment(request, expense_id):
    try:
        response = requests.delete(
            f"http://localhost:8000/ai/delete-payment/{expense_id}"
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

