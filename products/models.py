from django.db import models
from users.models import User

class Product_Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    sex = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to = Product_Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'name {self.name}, category {self.category.name}'



class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(bask.sum() for bask in self)




class Basket(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    objects = BasketQuerySet.as_manager()


    def __str__(self):
        return f'Корзина для пользователя {self.user.username}, Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    number = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'Заказ № {self.number}'