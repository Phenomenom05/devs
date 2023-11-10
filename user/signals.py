from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user=user,
            name=user.first_name,
            email=user.email,
            username=user.username,

        )
        subject = f"Hey {profile.name} Welcome to Dev search"
        message = "We are happy you are here"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email]
        )


def update_profile(sender, created, instance, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username
        user.email = profile.email
        user.save()


def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_profile, sender=Profile)
post_save.connect(update_profile, sender=Profile)