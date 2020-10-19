from django.shortcuts import render

# Create your views here.
from .tasks import order_created
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
#from . import telegram
import telepot

#Anin
#token = '1305283356:AAHg4mWw6KOK5QnJOBGsfRIlRr_XvEezXC8'

#my token
token = '983548097:AAGozXlJbKd4-bxzsz6ZMtuSTFQMPguu7pc'
#token = '389460165:AAEimDJ0HY3tJk9sd9HX1iHvjjUIG0hhAtM'

#Anin

#my_id = 397019375
#my test
my_id = 672574518
telegramBot = telepot.Bot(token)

def send_message(text):
  telegramBot.sendMessage(my_id, text, parse_mode="Markdown")



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            
            print(name)
            print(phone)
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['rp'],
                                         quantity=item['quantity'],
                                         rouse=item['rouse'],
                                         color=item['color'],
                                         color_type1=['color_type1'],
                                         color_type2=['color_type2'],
                                         color_type3=['color_type3'],
                                         )
                rouse = item['rouse']
                color = item['color']
                price = item['rp']
                product = item['product']
                color_type = ' ' + item['color_type1'] + ', ' + item['color_type2'] + ', ' + item['color_type3']
                print(rouse)
                print(color)
                print(color_type)
                message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " +str(name) +"\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "КОЛИЧЕСТВО РОЗ: " + str(rouse) + "\n" + "КОЛИЧЕСТВО ЦВЕТА :" + str(color) + "\n" + "ЦВЕТ/А: " + str(color_type) + "\n" + "ЦЕНА: " + str(price) +"\n" + "НАЗВАНИЕ ТОВАРА: " + str(product)
                send_message(message)
                #print(send_message(message))

            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})

