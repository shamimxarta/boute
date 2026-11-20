from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique =True)
    description = models.TextField(blank= True)
    is_active = models.BooleanField(default= True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name= "foods",
        )
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    image = models.ImageField(
        upload_to="foods/",
        blank = True,
        null = True,
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    