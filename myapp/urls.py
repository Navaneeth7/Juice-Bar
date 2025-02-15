from django.urls import path
from .views import *
app_name='myapp'

urlpatterns=[
    path('',homepage,name='homepage'),
    path('cartpage/',cartPage,name='cartpage'),
    path('orders/',orders,name='orders'),
    #path('login/',login,name='login'),
    #path('signup/',signup,name='signup'),
    # path('milkshakes/',milkshakes,name='milkshakes'),
    # path('fruitjuices/',fruitjuices,name='fruitjuices'),
    # path('hotbeverages/',hotbeverages,name='hotbeverages'),
    # path('softdrinks/',softdrinks,name='softdrinks'),
    # path('energydrinks/',energydrinks,name='energydrinks'),
    # path('mocktails/',mocktails,name='mocktails'),
    # path('beers/',beers,name='beers'),
    # path('wines/',wines,name='wines'),
    path('category/<int:category_id>/', category_view, name='category_view'),
    path('addtocart/<int:id>',addToCart,name='addtocart'),
    path('update_cart',update_cart,name='update_cart'),
    path('delete_item',delete_item,name='delete_item'),
    path('place_order/', place_order, name='place_order'),
    path('offer_milk/<int:d>/', offer_milk, name='offer_milk'),

    
]