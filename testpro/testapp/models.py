from __future__ import unicode_literals
from django.db import models

#Create your models here.
class user_details(models.Model):
    name=models.CharField(max_length=10)
    password=models.IntegerField()
    def __unicode__(self):
        return self.name
class user_additional_data(models.Model):
    add=models.OneToOneField(user_details,on_delete=models.CASCADE,primary_key=True,related_name='extra')
    address=models.CharField(max_length=100)
    phone_number=models.IntegerField()
