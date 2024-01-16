from django.contrib import admin

from products.models import Product_Category, Product, Basket

admin.site.register(Product)
admin.site.register(Product_Category)
admin.site.register(Basket)
