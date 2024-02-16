from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    
    def __str__(self):
        return self.name
