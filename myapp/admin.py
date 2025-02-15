from django.contrib import admin
from .forms import *
from .models import *
# Register your models here.
class categoriesAdmin(admin.ModelAdmin):
    list_display=['image','heading','product1','product2','product3','product4','product5','product6','product7','product8','product9','product10',]

class productsAdmin(admin.ModelAdmin):
    list_display=['image','productName','productPrice','quantity','Discount','Category']

class cartAdmin(admin.ModelAdmin):
    list_display=['product','image','quantity','price']

admin.site.register(Categories,categoriesAdmin)
admin.site.register(products,productsAdmin)
admin.site.register(cart,cartAdmin)

#Userdata Model
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']

# Correct way to register the model and admin class
admin.site.register(CustomUser, UserAdmin)
