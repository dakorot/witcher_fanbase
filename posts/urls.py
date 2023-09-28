from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top', views.top, name='top'),
    path('latest', views.latest, name='latest')
]
