from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save



que_choices = (
    ('Programming','Programming'),
    ('Technology', 'Technology'),
    ('Products', 'Products'),
    ('Science', 'Science'),
    ('Bussiness', 'Bussiness'),
    ('Educations', 'Educations'),
    ('GK', 'GK'),
    ('Space', 'Space'),
    ('Health', 'Health'),
    ('Others', 'Others'),
)
# Create your models here.
class QuestionsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(max_length=300)
    que_category = models.CharField(max_length=30, choices=que_choices, default='Others')
    que_details = models.TextField(max_length=4000, null=True, blank=True)
    que_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = QuestionsModel.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)