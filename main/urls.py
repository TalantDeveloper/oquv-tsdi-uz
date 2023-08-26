from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('mamuriyat', views.mamuryat, name='mamuriyat'),
    path('xodim', views.xodim, name='xodim'),
]
