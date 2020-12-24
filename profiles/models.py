import datetime
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

# class Project(models.Model):
# 	project_id = models.AutoField(primary_key=True)
# 	title = models.CharField(max_length=100)
# 	summary = models.CharField(max_length=100)
# 	description = models.CharField(max_length=100)
# 	constructor_id = models.CharField(max_length=100)
# 	project_manager_id = models.CharField(max_length=100)
# 	risk_manager_id = models.CharField(max_length=100)
# 	start_date = models.CharField(max_length=100)
# 	estimated_end_date = models.CharField(max_length=100)
# 	end_date = models.CharField(max_length=100)
# 	status = models.CharField(max_length=100)
# 	site_address = models.CharField(max_length=100)
# 	site_city = models.CharField(max_length=100)
# 	site_state = models.CharField(max_length=100)
# 	site_zip = models.CharField(max_length=100)
# 	site_country = models.CharField(max_length=100)
# 	site_phone1 = models.CharField(max_length=100)
# 	site_phone2 = models.CharField(max_length=100)
# 	site_fax = models.CharField(max_length=100)
# 	site_webpage = models.CharField(max_length=100)
# 	site_email = models.CharField(max_length=100)
# 	PMO_address = models.CharField(max_length=100)
# 	PMO_city = models.CharField(max_length=100)
# 	PMO_state = models.CharField(max_length=100)
# 	PMO_zip = models.CharField(max_length=100)
# 	PMO_country = models.CharField(max_length=100)
# 	PMO_phone1 = models.CharField(max_length=100)
# 	PMO_phone2 = models.CharField(max_length=100)
# 	PMO_fax = models.CharField(max_length=100)
# 	PMO_webpage = models.CharField(max_length=100)
# 	PMO_email = models.CharField(max_length=100)
# 	photos = models.FileField(upload_to='uploads/')
# 	notes = models.CharField(max_length=100)
# 	attachments = models.FileField(upload_to='uploads/')


# class Claim(models.Model):
# 	claim_id = models.AutoField(primary_key=True)
# 	project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=100)
# 	status = models.CharField(max_length=100)
# 	category = models.CharField(max_length=100)
# 	priority = models.CharField(max_length=100)
# 	date_generated = models.DateField(default=datetime.now)
# 	due_date = models.DateField(default=datetime.now)
# 	assigned_owner = models.CharField(max_length=100)
# 	assigned_PM = models.CharField(max_length=100)
# 	assigned_RM = models.CharField(max_length=100)
# 	assigned_SubContractor = models.CharField(max_length=100)
# 	related_claims = models.CharField(max_length=100)
# 	knowledge_base = models.CharField(max_length=100)
# 	key_words = models.CharField(max_length=100)
# 	attachments = models.FileField(upload_to='uploads/')
# 	notes = models.CharField(max_length=100)


# class Message(models.Model):
# 	message_id = models.AutoField(primary_key=True)
# 	claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)
# 	from_ = models.CharField(max_length=100, db_column='from')
# 	to = models.CharField(max_length=100)
# 	body = models.CharField(max_length=65536)
# 	date_sent = models.CharField(max_length=100)
# 	status = models.CharField(max_length=100)
# 	attachments = models.FileField(upload_to='uploads/')


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
