from django.contrib import admin
from .models import Article, Api_Urls
from django.contrib.admin import AdminSite

#rename the admin header
admin.site.site_header = 'Twenty20Disasters'

# Register your models here.
admin.site.register(Article)
admin.site.register(Api_Urls)