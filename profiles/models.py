from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

class UserProfile(models.Model):
    """ This is a user profile model for maaintaining
        delivery information and past order history (if any)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ To create or update the user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    # For existing user - Will just save the profile
    instance.userprofile.save()