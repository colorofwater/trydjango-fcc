from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=False)
    price       = models.DecimalField(blank=True, null=True, max_digits=10000, decimal_places=2)
    summary     = models.TextField(blank=True)
    featured = models.BooleanField()