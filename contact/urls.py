from django.urls import path

from contact.views import contact_view, success_view

# from accounts.views import index

urlpatterns = [
    path('contact-form/', contact_view, name='contact_view'),
    path('success/', success_view, name='success'),
]
