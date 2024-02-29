from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User,UserProfile

## Implementing Django Signal.

@receiver(post_save, sender= User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created :
        #print("Create the User Profile")
        UserProfile.objects.create(user=instance)
        #print("User Profile is created")
    else:
        try:
        
            profile= UserProfile.objects.get(user = instance)
            profile.save()
        
        except:
            # Create the user profile if not exist
            UserProfile.objects.create(user=instance)
            #print("Profile did not exist but I created one")
        #print("User is updated")

#Presave Receiver

#@receiver(pre_save, sender=User)
#def pre_save_profile_receiver(sender, instance, **kwargs):
#    #print(instance.username, "this user is being saved" )
#    pass