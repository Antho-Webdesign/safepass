from django.contrib import admin

from contact.models import Contact, ContactAdmin

# Register your models here.
admin.site.register(Contact, ContactAdmin)
