"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from app.views import (index, ProductCartView, category_books,LoginView,RegisterView,ProfileView,LogoutView,Users,
                       ShowBooks,delete,RegisterAdminView,UpdateUserView,deleteBook,Create, add_cart,deleteCart)
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
     path('dashboard/',Users, name='dashboard'),
     path('delete/<int:id>/',delete,name = "delete"),
     path('delete-book/<int:id>/',deleteBook,name = "deleteBook"),
      path('delete-cart/<int:id>/',deleteCart,name = "deleteCart"),
     path('login/', LoginView.as_view(), name='login'),
     path('profile/', ProfileView.as_view(), name='profile'),
     path('logout/', LogoutView.as_view(), name='logout'),
     
     
    path('update_user/<int:id>/', UpdateUserView.as_view(), name='user_update'),
    path('register/', RegisterView.as_view(), name='register'),     
    path('register-admin/', RegisterAdminView.as_view(), name='admin_register'),
    path('',index,name='index'),
    path('dashboard/',ShowBooks,name='dashboard'),
    path('category/<int:category_id>/',category_books, name='category_books'),
    path('create-product',Create.as_view(), name='create_product'),
    path('batafsil/<int:product_id>/', ProductCartView.as_view(), name="batafsil"),
    path('cart/', add_cart, name ='cart'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
