from .models import New, Course, Faculty
from modeltranslation.translator import TranslationOptions, register


@register(New)
class NewTranslationOptione(TranslationOptions):
    fields = ('title', 'content')


@register(Course)
class CourseTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Faculty)
class FacultyTranslationOption(TranslationOptions):
    fields = ('name',)
