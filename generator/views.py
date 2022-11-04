import random

from django.shortcuts import render

from generator.models import GenPass


# Create your views here.

def password_home(request):
    if request.method == "POST":

        site = request.POST.get('site')
        if site == "":
            return render(request, 'generator/password-home.html')

        password_length = int(request.POST.get('length'))
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            context = {'message': message}
            return render(request, 'generator/password-home.html', context)

        else:
            numbers = '1234567890'
            small_letters = "qwertyuioplkjhgfdsazxcvbnm"
            prep = f"!@#$%^&**()_+{numbers}{small_letters}QWERTYUIOPASDFGHJKLMNBVCXZ"
            passwd = ''.join(random.sample(prep, k=password_length))
            print(passwd, site)
            p = GenPass.objects.create(site=site, passwords=passwd)
            p.save()
            context = {'password': passwd}
            return render(request, 'generator/success.html', context)

    return render(request, "generator/password-home.html")