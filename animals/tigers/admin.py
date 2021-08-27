from django.contrib import admin

from .models import Pages, Photos, News,  Videos, Photosets
admin.site.register(Pages)
admin.site.register(Photos)
admin.site.register(Photosets)
admin.site.register(News)
admin.site.register(Videos)

