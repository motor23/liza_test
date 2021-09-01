from django.db import models


class Videos(models.Model):
    photo = models.CharField('Фото', max_length=250)
    title = models.CharField('Название', max_length=250)
    date = models.DateField('Дата публикации')
    video = models.CharField('Видео', max_length=250)


class Photos(models.Model):
    small_photo = models.CharField('Маленькое фото', max_length=250)
    photo = models.CharField('Фото', max_length=250)
    title = models.CharField('Название', max_length=250)

    def __str__(self):
        return self.title


class Pages(models.Model):
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Статья')
    connecting_to_photos = models.ManyToManyField(Photos)
    connecting_to_videos = models.ManyToManyField(Videos)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('Название', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    photo = models.CharField('Главное фото', max_length=250)
    connecting_to_photos = models.ManyToManyField(Photos)
    connecting_to_videos = models.ManyToManyField(Videos)

    def __str__(self):
        return self.title


class Photosets(models.Model):
    title = models.CharField('Название', max_length=250)
    title_photo = models.CharField('Титульное фото', max_length=250)
    connecting_to_photos = models.ManyToManyField(Photos)

    def __str__(self):
        return self.title
