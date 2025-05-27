
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project', views.project, name='project'),
    path('calc', views.calc, name='calc'),
    path('weather', views.weather, name='weather'),
    path('tictactoe', views.tictactoe, name='tictactoe'),
]