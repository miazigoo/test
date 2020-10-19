from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, rouse=None,
        color=None, color_type=None,  rp=1, update_quantity=False,
        color_type2=None, color_type3=None, color_type1=None,):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'rp': str(rp),
                                     'rouse': str(rouse),
                                     'color': str(color),
                                     'color_type1': str(color_type1),
                                     'color_type2': str(color_type2),
                                     'color_type3': str(color_type3),
                                     }
            color_type = self.cart[product_id]['color_type1'] + self.cart[product_id]['color_type2'] + self.cart[product_id]['color_type3'] 
            rp = self.cart[product_id]['rp']                      
            print(rp, color_type)
            print(self.cart[product_id])
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            pass
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
            # self.cart[str(product.id)]['rouse'] = rouse
            # self.cart[str(product.id)]['color'] = color
            # self.cart[str(product.id)]['color_type1', 'color_type2', 'color_type3'] = color_type

        for item in self.cart.values():
            item['rp'] = Decimal(item['rp'])
            item['total_price'] = item['rp'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['rp']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
