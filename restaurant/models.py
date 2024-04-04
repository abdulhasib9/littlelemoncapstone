from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField( max_length=200)
    no_of_guests = models.IntegerField()
    booking_date =models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    title = models.CharField( max_length=200)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return self.title
    