from django.urls import path, include

from generator.views import password_home, coffre_fort

urlpatterns = [
    path('generer-mot-de-passe/', password_home, name='password-home'),
    path('coffre-fort/', coffre_fort, name='coffre-fort'),
]
