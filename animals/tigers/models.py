from django.db import models

class Pages(models.Model):
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Статья')
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField('Название', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    photo = models.CharField('Главное фото', max_length=250)

    def __str__(self):
        return self.title

class Videos(models.Model):
    title = models.CharField('Название', max_length=250)
    date = models.DateTimeField('Дата публикации')
    video = models.CharField('Видео', max_length=250)
    connecting_to_pages = models.ManyToManyField(
        Pages,
        through='Pages_Videos',
        through_fields=('video_id', 'page_id'),
    )
    connecting_to_news = models.ManyToManyField(
        News,
        through='News_Videos',
        through_fields=('video_id', 'news_id'),
    )

class Photos(models.Model):
    photo = models.CharField('Фото', max_length=250)
    title = models.CharField('Название', max_length=250)
    connecting_to_pages = models.ManyToManyField(
        Pages,
        through='Pages_Photos',
        through_fields=('photo_id', 'page_id'),
    )
    connecting_to_news = models.ManyToManyField(
        News,
        through='News_Photos',
        through_fields=('photo_id', 'news_id'),
    )

    def __str__(self):
        return self.title


class Photosets(models.Model):
    title = models.CharField('Название', max_length=250)
    title_photo = models.CharField('Титульное фото', max_length=250)
    connecting_to_photos = models.ManyToManyField(
        Photos,
        through='Photosets_Photos',
        through_fields=('photoset_id', 'photo_id'),
    )
    def __str__(self):
        return self.title

class Pages_Videos(models.Model):
    page_id = models.ForeignKey(Pages, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Videos, on_delete=models.CASCADE)

class News_Videos(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Videos, on_delete=models.CASCADE)

class Pages_Photos(models.Model):
    page_id = models.ForeignKey(Pages, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photos, on_delete=models.CASCADE)

class News_Photos(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photos, on_delete=models.CASCADE)

class Photosets_Photos(models.Model):
    photoset_id = models.ForeignKey(Photosets, on_delete=models.CASCADE)
    photo_id = models.ForeignKey(Photos, on_delete=models.CASCADE)


