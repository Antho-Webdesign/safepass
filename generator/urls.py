from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from safepass import settings
from user.forms import LoginForm
from user.views import RegisterView, view_profile, profile, CustomLoginView, ResetPasswordView, ChangePasswordView

# from accounts.views import index

urlpatterns = [

]
