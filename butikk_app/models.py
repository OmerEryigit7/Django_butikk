from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.

class ProductInfo(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='butikk_app/static/images')

    def if_duplicate(self):
        if ProductInfo.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Dette produktnavnet er allerede i bruk.'})