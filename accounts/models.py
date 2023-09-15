from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from .emails import send_account_activation_email
import uuid

# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    is_email_verifed = models.BooleanField(default=False)
    email_token = models.CharField(max_length=150, null=True, blank=True)
    profile_img = models.ImageField(upload_to='profile')



@receiver(post_save, sender=User)
def send_email_token(sender, instance, created,  **kwargs):
    
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email
            send_account_activation_email(email, email_token)
            
    except Exception as e:
        print(e)
                
                
            
    
    
    

 