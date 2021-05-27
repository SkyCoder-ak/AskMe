from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save

# Create your models here.
gender_choices = (
    ('Male','Male'),
    ('Female', 'Female'),
)
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    age = models.CharField(max_length=4, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=gender_choices, default='Male')
    profile_photo = models.ImageField(upload_to='profile/images')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserModel.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
