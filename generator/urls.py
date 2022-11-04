from django.urls import path

from generator.views import password_home

# from accounts.views import index

urlpatterns = [
    path('generer-mot-de-passe/', password_home, name='password-home'),
]
