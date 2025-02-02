from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.cache import cache
from google.cloud import translate_v2 as translate
from django.conf import settings

class FAQ(models.Model):
    question = models.TextField(_('Question'))
    answer = RichTextField(_('Answer'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question

    def get_translated_field(self, field, lang):
        cache_key = f'faq_{self.id}_{field}_{lang}'
        cached_value = cache.get(cache_key)

        if cached_value:
            return cached_value

        original_value = getattr(self, field)
        if lang == settings.LANGUAGE_CODE:
            return original_value

        translate_client = translate.Client()
        translation = translate_client.translate(
            original_value,
            target_language=lang
        )

        translated_value = translation['translatedText']
        cache.set(cache_key, translated_value, timeout=3600)  # Cache for 1 hour

        return translated_value

    def get_translated_question(self, lang):
        return self.get_translated_field('question', lang)

    def get_translated_answer(self, lang):
        return self.get_translated_field('answer', lang)

