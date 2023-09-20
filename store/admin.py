from django.contrib import admin

from .models import (
    HeadLines
)
# Register your models here.

class HeadLinesAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline', 'is_real']
    list_display_links = ['id', 'headline']

admin.site.register(HeadLines, HeadLinesAdmin)

