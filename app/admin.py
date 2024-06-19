from django.contrib import admin
from .models import Category, Product, Cart,Ahuthors,User,Seller,Client
admin.site.register([Category, Product,])
admin.site.register(Cart)
admin.site.register(Ahuthors)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Seller)
