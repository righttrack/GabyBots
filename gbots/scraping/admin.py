'''
Created on Oct 14, 2012

@author: jeffmay
'''
from django.contrib import admin
from scraping.models import WebSource, Article

admin.site.register(WebSource)
admin.site.register(Article)
