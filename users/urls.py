from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

from users.views import UserLoginView, UserLogoutView, RegisterView, UserUpdateView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]