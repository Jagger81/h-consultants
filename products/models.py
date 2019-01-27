# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/static/img/')

#create your models here.
class Product(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(storage=fs)

    def __str__(self):
        return self.name