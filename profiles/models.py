from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField
from django_countries.fields import CountryField

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=50, blank=True)
	location = models.CharField(max_length=30)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	address_1 = models.CharField(_("Address line 1"), max_length=128, default="1000 Chastain Rd NW, Kennesaw")
	address_2 = models.CharField(_("Address line 2"), max_length=128, blank=True)
	state = USStateField(_("state"), default="GA")
	zip_code = models.CharField(_("zip code"), max_length=5, default="30144")
	county = models.CharField(_("county"), max_length=128, default="Cobb County")
	country = CountryField(default="US")
	email_confirmed = models.BooleanField(default=False)

class OfficialProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=50, blank=True)
	location = models.CharField(max_length=30)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	organization = models.CharField(_("organization"), max_length=128, default="KSU")
	address_1 = models.CharField(_("Address line 1"), max_length=128, default="1000 Chastain Rd NW, Kennesaw")
	address_2 = models.CharField(_("Address line 2"), max_length=128, blank=True)
	state = USStateField(_("state"), default="GA")
	zip_code = models.CharField(_("zip code"), max_length=5, default="30144")
	county = models.CharField(_("county"), max_length=128, default="Cobb County")
	country = CountryField(default="US")
	email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

@receiver(post_save, sender=User)
def update_official_profile(sender, instance, created, **kwargs):
	if created:
		OfficialProfile.objects.create(user=instance)
	instance.profile.save()
