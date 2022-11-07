import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from generator.models import GenPass


def password_home(request):
    if request.method == "POST":
        site = request.POST.get('site')

        if site == "":
            message = "Veuillez entrer un site"
            return render(request, 'generator/password-home.html', {'message': message})

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
            user = request.user

            print(passwd, site, user)
            p = GenPass.objects.create(site=site, passwords=passwd, user=user)
            p.save()
            context = {'password': passwd}
            return render(request, 'generator/success.html', context)

    return render(request, "generator/password-home.html")


@login_required
def coffre_fort(request):
    password_list = get_object_or_404(GenPass, user=request.user)
    context = {'password': password_list}
    return render(request, 'generator/listalll.html', context)



