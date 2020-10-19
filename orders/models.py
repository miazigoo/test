from django.db import models

# Create your models here.
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        # общая сумма заказа
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    rouse = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    color_type1 = models.CharField(max_length=60)
    color_type2 = models.CharField(max_length=60)
    color_type3 = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity