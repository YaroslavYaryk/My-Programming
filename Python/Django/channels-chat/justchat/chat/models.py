from django.db import models
from django.contrib.auth import get_user_model
from django.forms import TimeField

User = get_user_model()


class Message(models.Model):

    author = models.ForeignKey(User, verbose_name=(
        "author_messages"), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.TimeField(auto_now=False, auto_now_add=True)

    def get_last_30_messages():
        return Message.objects.order_by("timestamp")[:30]

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.author.username
