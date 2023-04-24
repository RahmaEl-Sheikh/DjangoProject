# from django.db import models


# Create your models here.

# class Category(models.Model):
#     objects = None
#     name = models.CharField(max_length=100)
#     description = models.TextField()


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)


# class Order(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     shipping_address = models.TextField()
#     payment_method = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()

# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     address = models.CharField(max_length=255, blank=True)
#     phone_number = models.CharField(max_length=20, blank=True)

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # your other fields and methods here

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='romasite_users_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='romasite_users_permissions'
    )