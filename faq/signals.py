from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FAQ

@receiver(post_save, sender=FAQ)
def faq_post_save(sender, instance, created, **kwargs):
    # You can add any post-save logic here if needed
    pass

