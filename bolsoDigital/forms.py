from django import forms
from .models import Expenses
from decimal import Decimal, InvalidOperation

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['description', 'value', 'id_category', 'payment_method', 'is_recurring']

    def clean_value(self):
        value = self.data.get('value')
        if value:
            value = value.replace(',', '.')
        try:
            return Decimal(value)
        except (InvalidOperation, TypeError):
            raise forms.ValidationError("Informe um número válido.")
