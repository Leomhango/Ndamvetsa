from dataclasses import fields
from django.contrib import admin

from .models import Word

class WordAdmin(admin.ModelAdmin):
    fields = ('word', 'part_of_speech','description', 'inSentence')
    list_display = ('word', 'part_of_speech','description', 'inSentence')

admin.site.register(Word, WordAdmin)