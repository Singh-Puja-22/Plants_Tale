from django.db import models

from app.models import Plant
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.plant.name}'