from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('news/', views.news, name='news'),
    path('program/', views.program, name='program'),
    path('animal/', views.animal, name='animal'),
    path('history/', views.history, name='history'),
    path('premier/', views.premier, name='premier'),
    path('photos', views.photos, name='photos'),
]
