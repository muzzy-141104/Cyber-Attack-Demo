from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    orders = models.ManyToManyField('Order', related_name='buyer')
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='buyer',
    )


    def __str__(self):
        return self.username
    
class Order(models.Model):
    pass
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()
    stock = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.title