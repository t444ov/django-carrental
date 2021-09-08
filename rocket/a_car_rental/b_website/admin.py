from django.contrib import admin
from .models import Article, AboutUs


@admin.register(Article)
class Article(admin.ModelAdmin):

    class Meta:
        model = Article


@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):

    class Meta:
        model = AboutUs
