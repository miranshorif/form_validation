from django.db import models

# Create your models here.
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'FeMale')
    )
    
    username = models.CharField(max_length=50,unique=True)
    text = models.TextField(max_length=1000, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    time = models.DateTimeField(auto_now_add=True)