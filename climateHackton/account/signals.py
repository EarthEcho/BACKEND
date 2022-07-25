from django.conf import settings
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def user_profile_created(sender, created, instance, *args, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user)
