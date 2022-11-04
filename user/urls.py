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
    path(r'^oauth/', include('social_django.urls', namespace='social')),

    path('login/',
         CustomLoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html',
                                 authentication_form=LoginForm), name='login'),

    path('login-test/',
         CustomLoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html',
                                 authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    path('register/', RegisterView.as_view(), name='users-register'),
    path('myprofile/', view_profile, name='view_profile'),
    path('profile/', profile, name='users-profile'),
    path('login/', CustomLoginView.as_view(), name='users-login'),
    path('logout/', LogoutView.as_view(), name='users-logout'),
]
