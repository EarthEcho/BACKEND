from django.db import models


def updload_to(instance, filename):
    return f'education/%Y/%m/%d/{filename}'


class ClimateEducation(models.Model):
    """
    Climate Education Model
    """
    topic = models.CharField(max_length=300)
    articles = models.TextField(blank=True)
    image = models.ImageField(upload_to=updload_to, blank=True)
    video_url = models.URLField(max_length=255, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.topic} id of {str(self.id)}'

    class Meta:
        verbose_name = 'Climate Education'
        verbose_name_plural = 'Climate Education'


class ClimateFact(models.Model):
    """
    Climate Fact Model
    """
    facts = models.TextField(blank=True)
    image = models.ImageField(upload_to=updload_to, blank=True)
    url = models.URLField(max_length=255, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Climate Fact'
        verbose_name_plural = 'Climate Facts'
