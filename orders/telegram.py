import telepot

#token = '1354610517:AAHOWGFRbBNy13UUb2ot8NeNYgGZCpIdmDs'
token = '389460165:AAEimDJ0HY3tJk9sd9HX1iHvjjUIG0hhAtM'
my_id = 672574518
telegramBot = telepot.Bot(token)

def send_message(text):
	telegramBot.sendMessage(177914540, text, parse_mode="Markdown")


def form_valid(self, form):
    name = form.cleaned_data['name']
    phone = form.cleaned_data['phone']
    message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
    send_message(message)
    return super(LeadCreationView, self).form_valid(form)

def form_invalid(self, form):
    return redirect(self.get_success_url())