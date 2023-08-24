from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.

class Costomer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=50)

    
    def __str__(self):
        # return f'{self.user}'
        return str(self.name)


CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('Tw','Top Wear'),
    ('BW','Bottom Wear'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price= models.FloatField()
    discounted_price=models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return str(self.title)


class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)


    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel')

)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    costomer = models.ForeignKey(Costomer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50, choices = STATUS_CHOICES,default='Pending')
    

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
