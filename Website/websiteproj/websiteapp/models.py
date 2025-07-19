from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(blank=True)

    class Meta:
        db_table='contact'
    