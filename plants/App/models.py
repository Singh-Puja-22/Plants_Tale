from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=100, default="Not Available")
    price = models.FloatField(default=0)
    plant_type = models.CharField(max_length=100, default="Not Available")
    description = models.TextField(default="Not Available")
    sunlight_requirements = models.CharField(max_length=100, default="Not Available")
    watering_needs = models.CharField(max_length=100, default="Not Available")
    blooming_period = models.CharField(max_length=100, default="Not Available")
    height = models.CharField(max_length=100, default="Not Available")
    fragrance = models.CharField(max_length=100, default="Not Available")
    flower_color = models.CharField(max_length=100, default="Not Available")
    care_tips = models.TextField(default="Not Available")
    img = models.ImageField(upload_to='static/images', null=True)

    # The code below is to store the likes of each plant item 
    likes = models.ManyToManyField(User, related_name="msg_likes")

    def total_likes(self):
        return self.likes.count()