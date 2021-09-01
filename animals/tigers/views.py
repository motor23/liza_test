from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Pages, Photos, News,  Videos, Photosets

def page_handler(request, id):
    page = Pages.objects.get(id__exact=id)
    photos_obj = page.connecting_to_photos.all()
    videos_obj = page.connecting_to_videos.all()
    return page, photos_obj, videos_obj


def home_page(request):
    news = News.objects.order_by('date')[:2]
    photos = Pages.objects.get(id__exact=6).connecting_to_photos.all()
    return render(request, 'tigers/main_page.html', {'news': news, 'photos': photos})

def news(request):
    page, photos_obj, videos_obj = page_handler(request, 5)
    news = News.objects.all()
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    news_obj = paginator.get_page(page_number)
    return render(request, 'tigers/news.html', {'page': page, 'news_obj': news_obj,
                                                'videos_obj': videos_obj})

def program(request):
    page, photos_obj, videos_obj = page_handler(request, 1)
    return render(request, 'tigers/page_environment.html', {'page': page, 'photos_obj': photos_obj,
                                                            'videos_obj': videos_obj})


def animal(request):
    page, photos_obj, videos_obj = page_handler(request, 2)
    return render(request, 'tigers/page_environment.html', {'page': page, 'photos_obj': photos_obj,
                                                            "videos_obj": videos_obj})

def history(request):
    page, photos_obj, videos_obj = page_handler(request, 3)
    return render(request, 'tigers/page_environment.html', {'page': page, 'photos_obj': photos_obj,
                                                            "videos_obj": videos_obj})


def premier(request):
    page, photos_obj, videos_obj = page_handler(request, 4)
    return render(request, 'tigers/page_environment.html', {'page': page, 'photos_obj': photos_obj,
                                                            "videos_obj": videos_obj})

def publication(request, id):
    news = News.objects.get(id__exact=id)
    return render(request, 'tigers/publication.html', {'news': news,})

def album(request, id):
    photoset = Photosets.objects.get(id__exact=id)
    photos = photoset.connecting_to_photos.all()
    return render(request, 'tigers/photos.html', {'photos': photos})

def photosets(request):
    albums = Photosets.objects.all()
    albums_obj = []
    for album in albums:
        a = album.connecting_to_photos.all().count()
        albums_obj.append([album, a])
    return render(request, 'tigers/photosets.html', {'albums_obj': albums_obj})


def videos(request):
    video = Videos.objects.all()
    return render(request, 'tigers/videos.html', {'videos': video, })

