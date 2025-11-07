from django.urls import path
from . import views

app_name = 'bolsoDigital'

urlpatterns = [
    # Adicione suas rotas aqui
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('upload-payment/', views.upload_payment, name='upload_payment'),
    path('delete-payment/<int:expense_id>/', views.delete_payment, name='delete_payment'),
    path('edit/<int:id>/', views.edit_payment, name='edit_payment'),
    path('dashboard/', views.dashboard, name='dashboard'),

]