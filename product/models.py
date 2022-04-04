from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    inventory_quantity = models.IntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
