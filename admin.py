from django.contrib import admin
from . models import *

# Register your models here.
class costomeradmin(admin.ModelAdmin):
    list_display=['user','name','locality','city','zipcode','state']
admin.site.register(Costomer,costomeradmin)

class productadmin(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price','description','brand','category','product_image']
admin.site.register(Product,productadmin)

class cartadmin(admin.ModelAdmin):
    list_display=['user','product','quantity']
admin.site.register(Cart,cartadmin)

class orderplacedadmin(admin.ModelAdmin):
    list_display=['user','costomer','product','quantity','ordered_date','status']
admin.site.register(OrderPlaced,orderplacedadmin)


# STATUS_CHOICES = (
#     ('Accepted','Accepted'),
#     ('Packed','Packed'),
#     ('On the way','On the way'),
#     ('Deliverd','Deliverd'),
#     ('Cancel','Cancel')

# )

# class OrderPlaced(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     costomer = models.ForeignKey(Costomer,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     status=models.CharField(max_length=50, choices = STATUS_CHOICES,default='Pending')



