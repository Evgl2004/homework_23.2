from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from users.models import User


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