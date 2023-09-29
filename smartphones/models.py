from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "категории"

    title = models.CharField(max_length=128, db_index=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Smartphone(models.Model):
    class Meta:
        verbose_name_plural = "смартфоны"

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="категория", on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
