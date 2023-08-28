from django.contrib import admin
from .models import New, Course, Curriculum, Faculty
from modeltranslation.admin import TranslationAdmin


@admin.register(New)
class NewAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'create_at', 'image')
    list_display_links = ('id', 'title', 'create_at', 'image')
    search_fields = ('id', 'title')


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'sub_name']
    list_display_links = ['id', 'name', 'sub_name']
    search_fields = ['id', 'name', 'sub_name']


admin.site.register(Curriculum)
# class CurriculumAdmin(admin.ModelAdmin):
#     list_display = ['id', 'file']
#     list_display_links = ['id', 'file']
