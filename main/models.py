from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class New(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")  # Translation
    content = RichTextUploadingField(verbose_name="Content")  # Translation
    image = models.ImageField(upload_to="./news/", default="./news/news.png")

    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    sees = models.IntegerField(default=65)

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kurs")  # Translation

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")  # Translation
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Curriculum(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course, null=True, blank=True)
    file = models.FileField(upload_to="./oquv/")

    def __str__(self):
        return self.file.name


class CourseShip(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
