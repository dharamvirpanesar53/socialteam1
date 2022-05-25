from distutils.command.upload import upload
from django.db import models

# Create your models here.
class campaign(models.Model):
    
    title= models.CharField(max_length=100)
    des= models.TextField()
    com= models.TextField(null=True, blank=True)
    lin= models.TextField(null=True, blank=True)
    img= models.ImageField(upload_to= 'pics')
    approved = models.BooleanField('Approved',default=False)
    blank=True