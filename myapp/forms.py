from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from myapp.models import Cart


def __init__(self, *args, **kwargs):
    super(AddToCartForm, self).__init__(*args, **kwargs)
    self.fields['count', 'size', 'color'].required = True
    # self.fields['count'].widget.attrs['min'] = 1


SIZE_CHOICES = (
    ('', '-- choose a option --'),
    ('Size S', 'Size S'),
    ('Size M', 'Size M'),
    ('Size L', 'Size L'),
    ('Size XL', 'Size XL'),
)

COLOR_CHOICES = (
    ('', '-- choose a option --'),
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Grey', 'Grey'),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddToCartForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     user_id = kwargs.pop("user_id")
    #     super(AddToCartForm, self).__init__(*args, **kwargs)

    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'mtext-104 cl3 txt-center num-product'}),
        min_value=1, max_value=10, initial=1)
    size = forms.CharField(max_length=20,
                           widget=forms.Select(choices=SIZE_CHOICES, attrs={'class': 'js-select2'})
                           )
    color = forms.CharField(max_length=20, widget=forms.Select(choices=COLOR_CHOICES, attrs={'class': 'js-select2'}))
    # class Meta:
    #     model = Cart
    #     fields = ['count', 'size', 'color']
