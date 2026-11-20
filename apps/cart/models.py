from django.conf import settings
from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name="carts",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )

    food = models.ForeignKey(
        "menu.Food",
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveBigIntegerField(default=1)
    