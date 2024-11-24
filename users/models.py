from django.db import models
from django.contrib.auth.models import User   ###PREDIFINED Django USER Model
## Extend The User Model withProfile
import uuid



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True) # One User has One Profile
    username = models.CharField(max_length=200 , null=True,blank=True)
    location = models.CharField(max_length=200 , null=True,blank=True)
    name = models.CharField(max_length=200 , null=True,blank=True)
    email = models.EmailField(max_length=200 , null=True,blank=True)
    short_intro = models.TextField(null=True,blank=True)
    bio  = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True, upload_to='profiles/', default='profiles/user_default.png')
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_x = models.CharField(max_length=200 , null=True,blank=True)
    social_linkdin = models.CharField(max_length=200 , null=True,blank=True)
    social_youtube = models.CharField(max_length=200 , null=True,blank=True)
    social_website = models.CharField(max_length=200 , null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ['name'] # "-" orders by descending

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url=''
        return url
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete = models.CASCADE, null = True, blank=True)
    name = models.CharField(max_length=200 , null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.name)
    
    

    ######moved signals to signals.py

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.subject)
    
    class Meta:
        ordering = ['is_read','-created']


