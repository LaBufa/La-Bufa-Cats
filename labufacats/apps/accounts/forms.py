from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'username': 'Nome de Usuário',
            'email': 'Endereço de Email',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = ''
    
