from .models import Pages, Photos, Pages_Photos, News, Pages_Videos, Videos,Photosets,Photosets_Photos, News_Photos

def news_create():
    file = open("C:\\Users\\Xiaomi\\liza_test\\animals\\tigers\\templates\\tigers\\input\\news_input.txt", "r", encoding="utf-8")
    news = file.read().split("---")
    news_parts = []
    for n in news:
        news_parts.append(n.split("***"))
    news_parts.pop()
    for n_p in news_parts:
        publication = News(title=n_p[0], full_text=n_p[1], date=n_p[2][2:-2], photo=n_p[3][2:-2])
        publication.save()

def pages_creat():
    file = open("C:\\Users\\Xiaomi\\liza_test\\animals\\tigers\\templates\\tigers\\input\\pages_input.txt", "r", encoding="utf-8")
    pages = file.read().split("---")
    pages_parts = []
    for n in pages:
        pages_parts.append(n.split("****"))
    pages_parts.pop()
    for p_p in pages_parts:
        page = Pages(title=p_p[0][1:-1], text=p_p[1][1:-1])
        page.save()

def photoset_create():
    file = open("C:\\Users\\Xiaomi\\liza_test\\animals\\tigers\\templates\\tigers\\input\\photoset_input.txt", "r", encoding="utf-8")
    photosets = file.read().split("---")
    photosets_parts = []
    for n in photosets:
        photosets_parts.append(n.split("****"))
    photosets_parts.pop()
    for p_p in photosets_parts:
        photoset = Photosets(title=p_p[0][1:-1], title_photo=p_p[1][2:-2])
        photoset.save()

def photo_create():
    file = open("C:\\Users\\Xiaomi\\liza_test\\animals\\tigers\\templates\\tigers\\input\\input_photo.txt", "r", encoding="utf-8")
    photos = file.read().split("----")
    photos_parts = []
    for n in photos:
        photos_parts.append(n.split("****"))
    photos_parts.pop()
    for p_p in photos_parts:
        photo = Photos(photo=p_p[0][2:-2], title=p_p[1][1:-1])
        photo.save()

def photoset_photo_create():
    photos = Photos.objects.filter(title__exact='В Приморском крае специалисты спасли жизнь раненого тигрёнка')
    photoset = Photosets.objects.filter(title__exact='В Приморском крае специалисты спасли жизнь раненого тигрёнка')[0]
    for photo in photos:
        object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
        object.save()
    photos = Photos.objects.filter(title__exact='Выпуск Санды в дикую природу запланирован на май 2021 года')
    photoset = Photosets.objects.filter(title__exact='Выпуск Санды в дикую природу запланирован на май 2021 года')[0]
    for photo in photos:
        object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
        object.save()
    photos = Photos.objects.filter(title__exact='Тигрица Санда вернулась в дикую природу')
    photoset = Photosets.objects.filter(title__exact='Тигрица Санда вернулась в дикую природу')[0]
    for photo in photos:
        object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
        object.save()
    photo = Photos.objects.filter(title__exact='Главной задачей программы является изучение пространственной структуры популяции амурского тигра, перемещений и численности этих кошек на территории России')[0]
    photoset = Photosets.objects.filter(title__exact='Программа изучения амурских тигров')[0]
    object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
    object.save()
    photo = Photos.objects.filter(title__exact='Основная цель программы «Амурский тигр» - разработка научных основ для сохранения амурского тигра на территории российского Дальнего Востока')[0]
    photoset = Photosets.objects.filter(title__exact='Программа изучения амурских тигров')[0]
    object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
    object.save()
    photo = Photos.objects.filter(title__exact='Программа изучения амурского тигра на российском Дальнем Востоке – самостоятельный проект в рамках Постоянно действующей экспедиции РАН по изучению животных Красной книги Российской Федерации и других особо важных животных фауны России')[0]
    photoset = Photosets.objects.filter(title__exact='Программа изучения амурских тигров')[0]
    object = Photosets_Photos(photo_id=photo, photoset_id=photoset)
    object.save()

def pages_photo_create():
    photos = Photos.objects.filter(title__exact='Программа')
    pages = Pages.objects.filter(title__exact='ПРОГРАММА ИЗУЧЕНИЯ АМУРСКОГО ТИГРА НА РОССИЙСКОМ ДАЛЬНЕМ ВОСТОКЕ')[0]
    for photo in photos:
        object = Pages_Photos(photo_id=photo, page_id=pages)
        object.save()

def database_create():
    news_create()
    pages_creat()
    photo_create()
    photoset_create()
    photoset_photo_create()
    pages_photo_create()
