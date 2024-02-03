from django.db import models

class Admin(models.Model):
    adharno= models.BigIntegerField(primary_key=True,blank=False,unique=True)
    username= models.CharField(max_length=30,blank=False,unique=True)
    # blank = false means name cannot be blank.
    #unique = true means name should be unique.
    password=models.CharField(max_length=10,blank=False,unique=False)
    class Meta:
        db_table="admin_table"
