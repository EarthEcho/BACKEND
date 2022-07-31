import uuid
from django.db import models
from django.conf import settings


def updload_to(instance, filename):
    return f'profiles/%Y/%m/%d/{filename}'


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, default='Lagos')
    avatar_url = models.ImageField(
        upload_to=updload_to, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        name = self.user.get_short_name()
        return f'{name}\'s Profile'
