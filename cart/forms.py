from django import forms
from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
CHOICE_ROUSE = [(1, ''),('19 роз', '19 роз'),('27 роз', '27 роз'),('37 роз', '37 роз'), ("41 роза", "41 роза"),("51 роза", "51 роза"), ("61 роза", "61 роза"),('77 роз', '77 роз'), ("101 роза", "101 роза")]
CHOICES_S = [('Белый', 'Белый'), ('Голубой' , 'Голубой'), ('Желтый' , 'Желтый'), ('Шоколад' , 'Шоколад'), ('Персиковый' , 'Персиковый'),('Розовый' , 'Розовый'),('Сиреневый' , 'Сиреневый'),]
CHOICES_COLOR = [('1 цвет', '1 цвет'), ('2 цвета', '2 цвета'), ('3 цвета', '3 цвета')]

class CartAddProductForm(forms.Form):
	
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(
        attrs={'class': 'form-control'}))
    rouse = forms.ChoiceField(choices=CHOICE_ROUSE, widget=forms.Select(
        attrs={'class': 'form-control rouse'}))
    color = forms.ChoiceField(choices=CHOICES_COLOR, widget=forms.RadioSelect(
        attrs={'class': 'form-control'}))
    color_type1 = forms.ChoiceField(choices=CHOICES_S, widget=forms.RadioSelect(
        attrs={'class': 'form-control'}))
    color_type2 = forms.ChoiceField(required=False, choices=CHOICES_S, widget=forms.RadioSelect(
        attrs={'class': 'form-control'}))
    color_type3 = forms.ChoiceField(required=False, choices=CHOICES_S, widget=forms.RadioSelect(
        attrs={'class': 'form-control'}))
    rp = forms.DecimalField(max_digits=10, decimal_places=2)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)	
    # class Meta:
    #     model = Product
    #     fields = ('rouse','color','color_type')
    #     widgets = {
    #         'rouse': forms.Select(),
    #         'color': forms.RadioSelect(attrs={'class': 'form-check-input'}),
    #         'color_type': forms.RadioSelect(attrs={'class': 'form-check-input'}),

    #     }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['rouse'].widget.attrs.update({'class':'form-control'})
    #     self.fields['color'].widget.attrs.update({'type': 'radio'})
    #     self.fields['color'].widget.attrs.update({'name': 'inlineRadioOptions'})
    #     self.fields['color_type'].widget.attrs.update({'type': 'radio'})
    #     self.fields['color_type'].widget.attrs.update({'name':'inlineRadioOptions'})

        		