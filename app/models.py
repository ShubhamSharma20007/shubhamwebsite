from django.db import models

# Create your models here.

class Entry(models.Model):
    username =  models.CharField(max_length=52)
    useremail =  models.EmailField()
    textfield = models.CharField(max_length=512)
    
    
    def __str__(self):
        return self.username
