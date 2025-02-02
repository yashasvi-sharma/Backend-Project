from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')

