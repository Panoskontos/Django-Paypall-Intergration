from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

# Many to Many
class UserBasket(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} -- {self.user.username}'
