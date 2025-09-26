from django.urls import path
from . import views

app_name = 'bolsoDigital'

urlpatterns = [
    # Adicione suas rotas aqui
    path('expenses/', views.expenses_list, name='expenses_list'),
]