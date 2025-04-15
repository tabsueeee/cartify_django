from django.db import models
from django.contrib.auth.models import User
from item.models import Item

# Create your models here.
class Messages(models.Model):
    item = models.ForeignKey(Item, related_name= 'message', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='message')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at',]

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Messages, related_name='conversations', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)