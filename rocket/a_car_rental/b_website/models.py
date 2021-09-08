from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateField(default=timezone.now)
    # image = models.ImageField(upload_to='img/article_image/', null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'Articles'
        db_table = 'articles'

    def __str__(self):
        return f'{self.title}, {self.date_created}, {self.description}'


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateField(default=timezone.now)
    # image = models.ImageField(upload_to='img/about_us_image/', null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'About us'
        db_table = 'about_us'

    def __str__(self):
        return f'{self.title}, {self.date_created}, {self.description}'
