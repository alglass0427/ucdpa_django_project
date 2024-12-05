from django.db import models
from django.contrib.auth.models import User   ###PREDIFINED Django USER Model
## Extend The User Model withProfile
import uuid
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pathlib import Path
from django.conf import settings

from cloudinary_storage.storage import MediaCloudinaryStorage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True) # One User has One Profile
    username = models.CharField(max_length=200 , null=True,blank=True)
    location = models.CharField(max_length=200 , null=True,blank=True)
    name = models.CharField(max_length=200 , null=True,blank=True)
    email = models.EmailField(max_length=200 , null=True,blank=True)
    short_intro = models.TextField(null=True,blank=True)
    bio  = models.TextField(null=True,blank=True)

    profile_image = models.ImageField(null=True,blank=True, upload_to='profiles/', #storage=MediaCloudinaryStorage(),
                                    #   default=f"https://res.cloudinary.com/{os.getenv('CLOUDINARY_CLOUD_NAME')}/image/upload/v12345678/profiles/user_default.png"
                                      default="https://res.cloudinary.com/dw32qih2n/image/upload/v1733050419/user_default_jgcypw.png"
                                           
                                      )
    
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
        BASE_DIR = Path(__file__).resolve().parent.parent
        os.path.join(BASE_DIR, 'templates')
        try:
            url = self.profile_image.url
            # url= "https://res.cloudinary.com/dw32qih2n/image/upload/v1733050419/user_default_jgcypw.png"
            
        except:
            # url= settings.MEDIA_URL + 'profiles/user_default.png'
            # print (settings.MEDIA_ROOT,'profiles/user_default.png')
            # url= "https://res.cloudinary.com/dw32qih2n/image/upload/v1733050419/user_default_jgcypw.png"
            url = ''
            # url = f"/default/{os.path.basename(default_path)}"

            # url= 'https://res.cloudinary.com/dw32qih2n/image/upload/v1733048687/user_default_xdrj9k.png'
                    # https://res.cloudinary.com/dw32qih2n/image/upload/v1733048687/user_default_xdrj9k.png
                    # https://res.cloudinary.com/dw32qih2n/image/upload/v1733048349/images/profiles/iron_man_pthgql.jpg
                    
                    
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


