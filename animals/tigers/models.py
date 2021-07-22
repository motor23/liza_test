from django.db import models

class Pages(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Статья')

class News(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    main_photo = models.ImageField('Главное фото')

class Videos(models.Model):
    title = models.CharField('Название', max_length=50)
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
    photo = models.ImageField('Фото')
    date = models.DateTimeField('Дата публикации')
    title = models.CharField('Название', max_length=50)
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

class Photosets(models.Model):
    title = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дата публикации')
    connecting_to_photos = models.ManyToManyField(
        Photos,
        through='Photosets_Photos',
        through_fields=('photoset_id', 'photo_id'),
    )

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


