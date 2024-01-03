from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView

from users.models import User
from users.forms import UserRegisterForm, UserForm

from django.core.mail import send_mail
from config import settings


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    # model = User
    #
    # success_url = reverse_lazy('users:users')


class UserLogoutView(LogoutView):
    pass
    # model = User
    #
    # success_url = reverse_lazy('users:users')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрировалась на нашей платформе! Добро пожаловать!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

