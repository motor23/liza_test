from django.shortcuts import render

from django.http import HttpResponse
from .models import Pages, Photos, Pages_Photos, News, Pages_Videos, Videos,Photosets,Photosets_Photos, News_Photos

def home_page(request):
    news = News.objects.all()
    photos = Photos.objects.all()
    return render(request, 'tigers/home_page.html', {'news': news, 'photos': photos})

def news(request):
    page = Pages.objects.extra(where=["title='НОВОСТИ ПРОЕКТА'"])[0]
    pages_photos = Pages_Photos.objects.filter(page_id__exact=page)
    l_p = len(pages_photos)
    photos = [pp.photo_id for pp in pages_photos]
    news = News.objects.all()
    l_n = len(news)//3 + 1
    pages_videos = Pages_Videos.objects.filter(page_id__exact=page)
    l_v = len(pages_videos)
    videos = [vv.video_id for vv in pages_videos]
    return render(request, 'tigers/news.html', {'title': page, 'pages_photos': pages_photos, 'count_p': l_p,
                                                'photos': photos, 'news': news, 'count_v': l_v,
                                                'videos': videos, 'l_n': l_n},)

def program(request):
    page = Pages.objects.extra(where=["title='ПРОГРАММА ИЗУЧЕНИЯ АМУРСКОГО ТИГРА НА РОССИЙСКОМ ДАЛЬНЕМ ВОСТОКЕ'"])[0]
    pages_photos = Pages_Photos.objects.filter(page_id__exact=page)
    l = len(pages_photos)
    photos = [pp.photo_id for pp in pages_photos]
    pages_videos = Pages_Videos.objects.filter(page_id__exact=page)
    count_v = len(pages_videos)
    videos = [vv.video_id for vv in pages_videos]
    return render(request, 'tigers/pattern.html', {'title': page, 'pages_photos': pages_photos, 'count_p': l,
                                                   'photos': photos, 'videos': videos, 'count_v': count_v},)

def animal(request):
    page = Pages.objects.extra(where=["title='АМУРСКИЙ ТИГР'"])[0]
    pages_photos = Pages_Photos.objects.filter(page_id__exact=page)
    l = len(pages_photos)
    photos = [pp.photo_id for pp in pages_photos]
    pages_videos = Pages_Videos.objects.filter(page_id__exact=page)
    count_v = len(pages_videos)
    videos = [vv.video_id for vv in pages_videos]
    return render(request, 'tigers/pattern.html', {'title': page, 'pages_photos': pages_photos, 'count_p': l,
                                                   'photos': photos, 'videos': videos, 'count_v': count_v}, )

def history(request):
    page = Pages.objects.extra(where=["title='ИСТОРИЯ ИЗУЧЕНИЯ АМУРСКИХ ТИГРОВ В РОССИИ'"])[0]
    pages_photos = Pages_Photos.objects.filter(page_id__exact=page)
    l = len(pages_photos)
    photos = [pp.photo_id for pp in pages_photos]
    pages_videos = Pages_Videos.objects.filter(page_id__exact=page)
    count_v = len(pages_videos)
    videos = [vv.video_id for vv in pages_videos]
    return render(request, 'tigers/pattern.html', {'title': page, 'pages_photos': pages_photos, 'count_p': l,
                                                   'photos': photos, 'videos': videos, 'count_v': count_v}, )


def premier(request):
    page = Pages.objects.extra(where=["title='РАБОЧАЯ ПОЕЗДКА ВЛАДИМИРА ПУТИНА В УССУРИЙСКИЙ ЗАПОВЕДНИК'"])[0]
    pages_photos = Pages_Photos.objects.filter(page_id__exact=page)
    l = len(pages_photos)
    photos = [pp.photo_id for pp in pages_photos]
    pages_videos = Pages_Videos.objects.filter(page_id__exact=page)
    count_v = len(pages_videos)
    videos = [vv.video_id for vv in pages_videos]
    return render(request, 'tigers/pattern.html', {'title': page, 'pages_photos': pages_photos, 'count_p': l,
                                                   'photos': photos, 'videos': videos, 'count_v': count_v}, )


def photos(request):
    albums = Photosets.objects.all()
    albums_photos = Photosets_Photos.objects.all()

    return render(request, 'tigers/photo.html', {'albums': albums, 'albums_photos': albums_photos})



def album(request, id = id):
    photos_photoset = Photosets_Photos.objects.filter(photoset_id__exact=id)
    photos = [pp.photo_id for pp in photos_photoset]
    return render(request, 'tigers/album.html', {'photos': photos})

def publication(request, id = id):
    news_photos = News_Photos.objects.filter(news_id__exact=id)
    photos = [pp.photo_id for pp in news_photos]
    news = News.objects.filter(id__exact=id)[0]
    return render(request, 'tigers/publication.html', {'photos': photos, 'news': news})
