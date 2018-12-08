from django.urls import path
from . import views


app_name = "Twitter"
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.Qlogin.as_view(), name='index'),
    path('path/', views.PostLogin.as_view(), name='login-quickly'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign-up/', views.SignupView.as_view(), name='sign-up'),
    path('home/', views.PostView.as_view(), name='home')
    ]