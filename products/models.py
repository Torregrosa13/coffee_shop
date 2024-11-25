from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='nombre')
    desc = models.TextField(max_length=200, verbose_name='desc')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True, verbose_name='disponible')
    image = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='fotos')


    def __str__(self):
        return self.name