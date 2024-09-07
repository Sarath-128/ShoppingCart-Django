from django.db import models

# Create your models here.

class appl(models.Model):
    
    item=models.CharField(max_length=100)

    price=models.IntegerField()

    image=models.ImageField(upload_to='book_media')

    quantity=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.item)
