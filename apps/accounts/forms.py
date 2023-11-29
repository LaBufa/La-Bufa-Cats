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
    
class AdocaoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    idade = forms.CharField(max_length=20)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    motivacao = forms.CharField(widget=forms.Textarea, required=False)
    concordo = forms.BooleanField()
