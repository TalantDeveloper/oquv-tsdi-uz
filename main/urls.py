from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('mamuriyat', views.mamuryat, name='mamuriyat'),
    path('new/<int:pk>/', views.new, name='new'),
    path('xodim', views.xodim, name='xodim'),
    path('oquv_reja', views.oquv_reja_view, name="oquv_reja"),
]
