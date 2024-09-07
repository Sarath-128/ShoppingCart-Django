from django.db import models
from myapp.models import appl
from django.contrib.auth.models import User

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(appl)

class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(appl,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
