from django.db import models
from django.urls import reverse_lazy
from django.conf import settings

import misaka

from groups.models import Group
 # Create models here
 # POSTS MODELS.PY

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse_lazy('posts: single',kwargs={'User':self.user,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']
