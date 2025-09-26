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
                "http://localhost:8000/upload-payment",
                files={'file': (file.name, file.read(), file.content_type)}
            )
            if response.status_code == 200:
                messages.success(request, "Comprovante enviado com sucesso!")
            else:
                messages.error(request, f"Erro ao enviar: {response.text}")
        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
    return redirect('bolsoDigital:expenses_list')
