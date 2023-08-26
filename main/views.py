from django.shortcuts import render


def welcome_view(request):
    return render(request, 'main/welcome.html')


def mamuryat(request):
    return render(request, 'main/mamuryat.html')


def xodim(request):
    return render(request, 'main/xodim.html')