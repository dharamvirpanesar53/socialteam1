from distutils.command.upload import upload
from django.db import models

# Create your models here.
class campaign(models.Model):
    
    title= models.CharField(max_length=100)
    des= models.TextField()
    img= models.ImageField(upload_to= 'pics')
    approved = models.BooleanField('Approved',default=False)