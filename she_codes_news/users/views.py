from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ViewAccount(CreateView):
    model = CustomUser
    fields = ['username', 'email']
    success_url = reverse_lazy('viewAccount')
    template_name = 'registration/viewAccount.html'
