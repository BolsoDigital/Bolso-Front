from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Telefone",
        widget=forms.TextInput(attrs={'id': 'id_phone_number'}) # Garante o ID correto pro JS pegar
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "phone_number")

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')

        if phone:

            phone = phone.replace('+', '').replace(' ', '').replace('-', '').strip()

            if User.objects.filter(phone_number=phone).exists():
                raise forms.ValidationError("Este número de telefone já está cadastrado.")
        
        return phone

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")