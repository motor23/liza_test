from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_page, name='index'),
    path('news/', views.news, name='news'),
    path('news/<int:id>', views.publication, name='publication'),
    path('program/', views.program, name='program'),
    path('animal/', views.animal, name='animal'),
    path('history/', views.history, name='history'),
    path('premier/', views.premier, name='premier'),
    path('multimedia/photos/', views.photos, name='photos'),
    path('multimedia/photos/<int:id>', views.album, name='album'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

