from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="cat_image", null= True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="product_images")
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    @property
    def get_price(self):
        return self.price * self.quantity

class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}"
    

class Ahuthors(models.Model):
    name = models.CharField(max_length=255)
    biography =models.CharField(max_length=2550)
    image = models.ImageField(upload_to='author_image')


# Create your models here.




class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('client', 'client'),
        ('app', 'app'),
        ('admin', 'Admin'),
    )
    

    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return f'{self.user.first_name}'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return f'{self.user.first_name}'
    
