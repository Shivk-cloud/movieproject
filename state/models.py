from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=200)
    length=models.IntegerField()
    release_year=models.IntegerField()

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    first_name=models.CharField(max_length=20)  
    last_name=models.CharField(max_length=20) 
    phone=models.PositiveIntegerField()

    def __str__(self):
        return self.first_name+' '+self.last_name
    
