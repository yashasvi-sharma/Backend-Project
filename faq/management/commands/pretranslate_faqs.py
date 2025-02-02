from django.core.management.base import BaseCommand
from faq.models import FAQ
from django.conf import settings

class Command(BaseCommand):
    help = 'Pre-translate all FAQs to supported languages'

    def handle(self, *args, **options):
        faqs = FAQ.objects.all()
        languages = [lang[0] for lang in settings.LANGUAGES if lang[0] != settings.LANGUAGE_CODE]

        for faq in faqs:
            for lang in languages:
                faq.get_translated_question(lang)
                faq.get_translated_answer(lang)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully pre-translated FAQ: {faq.question}'))

        self.stdout.write(self.style.SUCCESS('All FAQs have been pre-translated'))

