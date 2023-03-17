from django.db import models
from django.contrib.auth.models import User
from applications.gymkhana.models import Club_info

# Create your models here.
class Post(models.Model):
    fileTypeOption = (
    ("image", "image"),
    ("video", "video"),
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club_info , on_delete=models.CASCADE)
    filetype = models.CharField(max_length=32 , choices=fileTypeOption)
    file = models.FileField(upload_to="FusionIIIT\media\clubfeeds")
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()