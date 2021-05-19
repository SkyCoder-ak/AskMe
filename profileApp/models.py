from django.db import models

# Create your models here.
class UserModel(models.Model):
    fullname = models.CharField(max_length=60)
    dis_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.fullname
    
