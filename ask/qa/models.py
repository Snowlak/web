from django.db import models
import django.contrib.auth.models as user


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(user.User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(user.User,
                                   related_name='question_like_user')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question, null=True,
                                    on_delete=models.SET_NULL)
    author = models.ForeignKey(user.User, on_delete=models.CASCADE)
