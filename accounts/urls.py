from django.urls import path
from .views import UserSignUpView, UserLoginView, UserLogoutView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user_signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]