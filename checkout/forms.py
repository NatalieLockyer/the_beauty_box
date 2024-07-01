from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """ Order form fields we want to render """
    discount_code = forms.CharField(required=False, max_length=20, label='Discount Code')

    class Meta:
        model = Order 
        fields = ['full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county', 'discount_code',]

    def __init__(self, *args, **kwargs):
        """ This will add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field. """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
            'phone_number': 'Phone Number',    
           }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False