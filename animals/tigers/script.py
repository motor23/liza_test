import os
from faker import Faker
from .models import Pages, Photos,  News, Videos, Photosets
import random

def open_file(path):
    os.environ["HOME"] = os.getcwd()
    full_path = os.path.expanduser(path)
    file = open(full_path, "r", encoding="utf-8")
    elements = file.read().split("---")
    elements_parts = []
    for n in elements:
        elements_parts.append(n.split("****"))
    elements_parts.pop()
    return elements_parts


photos_link = ['tigers/news.jpeg', 'tigers/news1.jpeg', 'tigers/news2.jpeg', 'tigers/news3.jpeg', 'tigers/news_4.jpeg',
               'tigers/news_5.jpeg', 'tigers/news_6.jpeg', 'tigers/news_7.jpeg', 'tigers/news_8.jpeg',
               'tigers/news_9.jpeg', 'tigers/news_10.jpeg']

def new_create():
    fake = Faker('ru_RU')
    title = fake.text()
    full_text = fake.text()
    date = fake.date()
    photo = random.choice(photos_link)
    publication = News(title=title, full_text=full_text, date=date, photo=photo)
    publication.save()

def pages_create():
    path = "~\\tigers\\input\\pages_input.txt"
    pages_parts = open_file(path)
    for p_p in pages_parts:
        page = Pages(id=int(p_p[0]), title=p_p[1][1:-1], text=p_p[2][1:-1])
        page.save()

def photoset_create():
    fake = Faker('ru_RU')
    title = fake.text()
    photo = random.choice(photos_link)
    photoset = Photosets(title=title, title_photo=photo)
    photoset.save()


photos = ['tigers/photo1', 'tigers/photo2', 'tigers/photo3']


def photo_create():
    fake = Faker('ru_RU')
    small_photo = random.choice(photos)
    photo = small_photo + '_big.jpeg'
    title = fake.text()
    photo = Photos(small_photo=small_photo +'.jpeg', photo=photo, title=title)
    photo.save()

def pages_photo_create(id):
    page = Pages.objects.get(id__exact=id)
    photos = Photos.objects.all()
    photo = random.choice(photos)
    page.connecting_to_photos.add(photo)

def photosets_photos_create():
    photosets = Photosets.objects.all()
    photos = Photos.objects.all()
    for photoset in photosets:
        for photo in photos:
            photoset.connecting_to_photos.add(photo)

