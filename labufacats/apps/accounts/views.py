from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import UserForm
from .forms import AdocaoForm
from .models import Adocao
from django.http import HttpResponseRedirect
from .models import Post



class NotFoundView(View):
    def get(self, request, path):
        return HttpResponseNotFound("Página não encontrada.")

class PrincipalView(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name, {})


class CatalogoView(ListView):
    model = Post
    template_name = 'catalogo.html'
    context_object_name = 'posts'

class DetalhesView(DetailView):
    model = Post
    template_name = 'detalhes.html'
    context_object_name = 'post'
    
class AdocaoView(DetailView):
    model = Post
    template_name = 'adocao.html'
    context_object_name = 'post'
    
def processar_formulario(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Crie uma instância do modelo e salve os dados
            adocao = Adocao(
                nome=form.cleaned_data['nome'],
                idade=form.cleaned_data['idade'],
                email=form.cleaned_data['email'],
                telefone=form.cleaned_data['telefone'],
                motivacao=form.cleaned_data['motivacao'],
                concordo=form.cleaned_data['concordo']
            )
            adocao.save()
            messages.success(request, 'Formulário enviado com sucesso. Entraremos em contato com você via Email ou WhatsApp')
            return redirect('accounts:index')

    else:
        form = AdocaoForm()

    return render(request, 'accounts/adoção.html', {'form': form})


class RifasView(View):
    def get(self, request):
        template_name = 'rifas.html'
        return render(request, template_name, {})

class DoacaoView(View):
    def get(self, request):
        template_name = 'doacao.html'
        return render(request, template_name, {})

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        context = {'form': UserForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('accounts:index')
        context = {'form': form}
        return render(request, self.template_name, context)

class UserLoginView(View):
    template_name = 'user_login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login bem-sucedido.')
            return redirect('accounts:index')
        else:
            messages.error(request, 'Usuário e senha não cadastrados.')
            return render(request, self.template_name, {})

class UserProfileView(View):
    template_name = 'user_profile.html'

    def get(self, request):
        return render(request, self.template_name, {})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Você saiu do sistema.')
        return redirect('accounts:home')