from django.contrib import admin

from .models import Topic, Entry

"""Precisamos importar manualmente as models criadas para 
que elas apareçam no gerenciador do admin"""
admin.site.register(Topic)
admin.site.register(Entry)