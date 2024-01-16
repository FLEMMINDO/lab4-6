from products.views import contact,index, shop, about, shop_single, basket_add, basket_remove, make_order
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', shop, name = 'index'),
    path('category/<int:category_id>/', shop, name = 'category'),
    path('page/<int:page_number>/', shop, name = 'paginator'),
    path('order/make/', make_order, name = 'make_order'),
    path('baskets/add/<int:product_id>/', basket_add, name = 'basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name = 'basket_remove'),
]