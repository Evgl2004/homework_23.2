from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

from users.views import UserLoginView, UserLogoutView, RegisterView, UserUpdateView, activate_code, generate_new_password

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('activate/<str:code>', activate_code, name='activate'),
]