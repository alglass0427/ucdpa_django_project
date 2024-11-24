from django.db.models.signals import post_save ,  post_delete
# using signals with decorators
from django.dispatch import receiver
from .models import Profile , User
from django.core.mail import send_mail
from django.conf import settings
##TO ACTIVATE THE SIGNALS.py FILE it HAS TO BE ADDED TO 
        ## USERS APP   -  > app.py file


@receiver(post_save,sender = User)
def createProfile(sender,instance,created, **kwargs):   ### create only exists if the Object is created in that instance
    print('Create Profile Signal triggered  . . . ')
    if created:                 # User is the Sender  -  so this checks if the User is created
        user = instance         #  
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

        subject = 'Welcome to the Website'
        message = "Glad you joined -  Hope you enjoy"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )



@receiver(post_save, sender = Profile)
def updateUser(sender, instance, created , **kwargs):
    profile = instance
    user = profile.user
    if created == False:  ##THIS IS INCLUDED TO PREVENT THE SIGNALS TRIGGERING EACH OTHER 
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender = Profile)
def deleteUser(sender,instance, **kwargs):
    try:
        user = instance.user   ##   One to One   - - user.Profile is short hand for gettign the user from the Profile instance
        user.delete()
        print('Deleting user...')
    except:
        pass
    
# non Decorator
# post_save.connect(profileUpdated,sender=Profile)
# post_save.connect(UpdateUser,sender=Profile)
# post_delete.connect(deleteUser,sender=Profile)


