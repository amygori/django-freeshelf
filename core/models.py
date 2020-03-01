from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Book title: {self.title} author: {self.author}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
