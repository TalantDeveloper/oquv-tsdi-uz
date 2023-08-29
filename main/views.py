from django.shortcuts import render
from .models import Faculty, Course, Curriculum, New, Description, Requirement, StudentTable


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


def news_view(request):
    news = New.objects.all()
    return render(request, 'main/news.html', {'news': news})


def new(request, pk):
    new = New.objects.get(pk=pk)
    return render(request, 'main/new.html', {'new': new})


def tavsfinoma_view(request):
    descriptions = Description.objects.all()
    return render(request, 'main/tavsifnoma.html', {'descriptions': descriptions})


def talablar_view(request):
    requirements = Requirement.objects.all()
    return render(request, 'main/talablar.html', {'requirements': requirements})


def dars_jadval_view(request):
    faculties = Faculty.objects.all()
    courses = Course.objects.all()
    student_tables = StudentTable.objects.all()
    content = {
        'faculties': faculties,
        'courses': courses,
        'student_tables': student_tables
    }
    return render(request, 'main/jadval.html', content)
