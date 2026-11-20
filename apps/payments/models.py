from django.db import models

# Create your models here.

class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending", "در انتظار پرداخت"),
        ("success", "موفق"),
        ("failed", "ناموفق"),
        ("refunded", "برگشت داده شده"),
    ]

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.PROTECT,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    transaction_id = models.CharField(
        max_length=150,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)

    discount_percent = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    max_uses = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.code

class Review(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )

    food = models.ForeignKey(
        "menu.Food",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)