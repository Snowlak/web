from django.db import models
import django.contrib.auth.models as user
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class QuestionManager(models.Manager):
    def new(self):
        return self.all().order_by('-added_at')

    def popular(self):
        return self.all().order_by('-rating')


class Like(models.Model):
    user = models.ForeignKey(user.User, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Question(models.Model):
    title = models.CharField(default='', max_length=255)
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(user.User, on_delete=models.SET_NULL, null=True)
    likes = GenericRelation(Like)

    objects = QuestionManager()

    @property
    def total_like(self):
        return self.likes.count()


class Answer(models.Model):
    objects = models.Manager
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question, null=True,
                                    on_delete=models.SET_NULL)
    author = models.ForeignKey(user.User, on_delete=models.SET_NULL, null=True)
