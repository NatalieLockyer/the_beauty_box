from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ This will allow us to add and edit line items in
        the admin from within the order model. """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    """ These are all fields that will be calculated 
        by the order model. """
    readonly_fields = ('order_number', 'date',
                        'delivery_cost', 'order_total',
                        'grand_total', 'original_basket',
                        'stripe_pid',)

    """ Allows me to specify the order fields in the admin interface"""
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2',
              'county', 'delivery_cost', 'order_total', 'grand_total',
              'original_basket', 'stripe_pid',)

    """ Items to be displayed within the admin"""
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)