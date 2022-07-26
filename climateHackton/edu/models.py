from django.db import models


def updload_to(instance, filename):
    return f'education/%Y/%m/%d/{filename}'


class ClimateEducation(models.Model):
    """
    Climate Education Model
    """
    name = models.CharField(max_length=255)
    articles = models.TextField(blank=True)
    image = models.ImageField(upload_to=updload_to, blank=True)
    video_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Climate Education'
        verbose_name_plural = 'Climate Education'


class ClimateFact(models.Model):
    """
    Climate Fact Model
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=updload_to, blank=True)
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Climate Fact'
        verbose_name_plural = 'Climate Facts'
