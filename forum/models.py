from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from registration.models import Profile
# from propose_join.models import Clubs

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Comments(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Replies(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# Create your models here.
# class Question(models.Model):
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
#
# class Answer(models.Model):
#     answer_to = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="")
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
#
# class Comments(models.Model):
#     comment_to = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name="")
#     creater = models.ForeignKey(Users,on_delete=models.CASCADE,related_name="")
#     in_club = models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     text_content = models.TextField()
#     image = models.FilePathField()
#     video = models.FilePathField()
