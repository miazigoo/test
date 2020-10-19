from django.db import models

# Create your models here.
import os
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


def get_upload_path(instance, filename):
    #  задаем название файла названием slug`а продукта
    filename = instance.slug + '.' + filename.split('.')[1]  
    return os.path.join('images/', filename)


class Color(models.Model):
	"""docstring for RouseCount"""
	color = models.CharField(max_length= 100, default=None)
	def __str__(self):
		return '%s' % self.color



class RouseCount(models.Model):
	"""docstring for RouseCount"""
	rouse = models.IntegerField(default=41)
	def __str__(self):
		return '%s' % self.rouse
		

class ColorType(models.Model):
	"""docstring for RouseCount"""
	color_type = models.CharField(max_length=20)
	def __str__(self):
		return '%s' % self.color_type



class Product(models.Model):

	rouse = models.ForeignKey(RouseCount, related_name='rouses', on_delete=models.CASCADE, blank=True)
	color = models.ForeignKey(Color, related_name='colors', on_delete=models.CASCADE, blank=True)
	color_type = models.ForeignKey(ColorType, related_name='coltypes', on_delete=models.CASCADE, blank=True)
	color_type2 = models.ForeignKey(ColorType, related_name='coltypes2', on_delete=models.CASCADE, blank=True, null=True)
	color_type3 = models.ForeignKey(ColorType, related_name='coltypes3', on_delete=models.CASCADE, blank=True, null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])
