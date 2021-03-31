from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('login_form/', views.login_form, name="login_form"),
    path('logout/', views.logout_user, name="logout"),

    ]
