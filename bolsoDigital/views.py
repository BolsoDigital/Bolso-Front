from django.shortcuts import render
from .models import Expenses

def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', {'expenses': expenses})