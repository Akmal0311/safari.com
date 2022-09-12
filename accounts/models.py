from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/')
    is_verified = models.BooleanField(default=False)
    user_token = models.CharField(max_length=22, )
    gender = models.CharField(max_length=11, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)


class ShippingAddress(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    email = models.EmailField()
    full_name = models.CharField(max_length=111)
    address = models.CharField(max_length=333)
    state = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    phone_number = models.CharField(max_length=13)


class UserFavorites(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)+" : "+str(self.product)
