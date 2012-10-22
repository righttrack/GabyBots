'''
Created on Oct 14, 2012

@author: jeffmay
'''
from django.contrib import admin
from gbots.scraping.models import WebSource, Article

admin.site.register(WebSource)
admin.site.register(Article)
