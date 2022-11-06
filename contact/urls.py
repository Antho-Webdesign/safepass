from django.urls import path

from contact.views import contact_view, success_view

# from accounts.views import index

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
