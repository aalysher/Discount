from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Company, View


@receiver(post_save, sender=Company)
def get_counter_views(sender, instance, created, **kwargs):
    if created:
        View.objects.create(id=instance)
