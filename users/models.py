from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_to(instance, filename):
    return filename.format(filename=filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('-created_at',)

# RECEIVER TO TRIGGER CREATION OF PROFILE AFTER NEW USER IS CREATED


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('instance', sender)

    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
    else:
        instance.profile.save()
