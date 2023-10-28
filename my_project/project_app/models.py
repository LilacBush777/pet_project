from django.db import models
from django.urls import reverse


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    background = models.TextField(blank=True)
    photo_family = models.ImageField()
    photo_person = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

