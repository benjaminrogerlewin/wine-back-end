from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    

    def __str__(self):
        return self.username
    
class Wine(models.Model):
    producer = models.CharField(max_length=100)
    vintage = models.CharField(max_length=100)
    grape = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    rated = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.producer
    
class Rating(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField(validators=[
        MaxValueValidator(5.0),
        MinValueValidator(0.0)
    ])
    review = models.CharField(max_length=100)
    taste = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.review
    
