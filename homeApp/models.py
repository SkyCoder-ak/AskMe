from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
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
# model for questions
class QuestionsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(max_length=300)
    que_category = models.CharField(max_length=30, choices=que_choices, default='Others')
    que_details = models.TextField(max_length=2000, null=True, blank=True)
    que_date_time = models.DateTimeField(auto_now_add=True)
    que_views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.question
    

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = QuestionsModel.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile, sender=User)


# model for answers
class AnswersModel(models.Model):
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE, null=True, blank=True)
    ans_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    ans_date_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="answers_likes")

    def __str__(self):
        if self.answer != None:
            return self.answer[:100]

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = AnswersModel.objects.create(question=kwargs['instance'])
# post_save.connect(create_profile, sender=User)



class FollowModel(models.Model):
    u = models.OneToOneField(User, on_delete=models.CASCADE)
    followed_to = ManyToManyField(User, related_name='followed_users')

class Followers(models.Model):
    card_user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed_by = ManyToManyField(User, related_name='followed_by_users')