from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bolso Digital funcionando!")

# Adicione suas views aqui
# def expenses(request):
#     return render(request, 'bolsoDigital/expenses.html')