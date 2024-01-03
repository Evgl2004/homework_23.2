from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView

from users.models import User
from users.forms import UserRegisterForm, UserForm

from django.core.mail import send_mail
from config import settings

import uuid, random


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.code = str(uuid.uuid4())
        new_user.is_active = False

        new_user.save()

        send_mail(
            subject='Поздравляем с регистрацией!',
            message=f'Вы зарегистрировалась на нашей платформе!\n'
                    f'Добро пожаловать!\n'
                    f'Активация профиля: {reverse_lazy("users:activate", args=[new_user.code])}\n',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate_code(request, code):
    user = User.objects.get(code=code)

    if user is not None:
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('main:home'))

