from django.db import models
from django.contrib.auth.models import User
from applications.gymkhana.models import Club_info
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    fileTypeOption = (
    ("image", "image"),
    ("video", "video"),
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club_info , on_delete=models.CASCADE)
    filetype = models.CharField(max_length=32 , choices=fileTypeOption)
    file = models.FileField(upload_to="clubfeeds/")
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def like(self, user):
        if user not in self.liked_by.all():
            self.likes += 1
            self.liked_by.add(user)
            self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('addcomment', args=[str(self.post.id)])