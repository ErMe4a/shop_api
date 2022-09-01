from unicodedata import category
from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image =models.ImageField(upload_to='images', null = True, blank = True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


