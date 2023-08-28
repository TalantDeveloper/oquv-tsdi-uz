from django.shortcuts import render
from .models import Faculty, Course, Curriculum, New


def welcome_view(request):
    news = New.objects.all()[:4]
    content = {
        'news': news
    }
    return render(request, 'main/welcome.html', content)


def mamuryat(request):
    return render(request, 'main/mamuryat.html')


def xodim(request):
    return render(request, 'main/xodim.html')


def oquv_reja_view(request):
    faculties = Faculty.objects.all()
    course = Course.objects.all()
    curriculums = Curriculum.objects.all()
    content = {
        'faculties': faculties,
        'courses': course,
        'curriculums': curriculums,
    }
    return render(request, 'main/oquv_reja.html', content)


def new(request, pk):
    pass