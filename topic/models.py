from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        if len(self.text) < 50 :
            return f"Comment by {self.user.username} on {self.topic.title}: {self.text}"
        else:
            return f"Comment by {self.user.username} on {self.topic.title}: {self.text[:50]}"

