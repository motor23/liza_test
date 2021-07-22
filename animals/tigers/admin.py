from django.contrib import admin

from .models import Photos, Pages,Pages_Photos,Photosets_Photos, Photosets,News_Photos, Videos
from .models import News, News_Videos, Pages_Videos

admin.site.register(Pages)
admin.site.register(Pages_Photos)
admin.site.register(Photos)
admin.site.register(Photosets_Photos)
admin.site.register(Photosets)
admin.site.register(News)
admin.site.register(News_Photos)
admin.site.register(Videos)
admin.site.register(News_Videos)
admin.site.register(Pages_Videos)



