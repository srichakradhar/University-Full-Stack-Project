from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.us.forms import USStateField
from django_countries.fields import CountryField
from localflavor.us.models import STATE_CHOICES

class SignUpForm(UserCreationForm):
	username = forms.CharField(
		label='Username',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "username",
				"class": "form-control"
			}
		)
	)

	email = forms.EmailField(
		label='Email',
		max_length=255,
		required=True,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "email@gmail.com",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "••••••••",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "••••••••",
				"class": "form-control"
			}
		)
	)

	location = forms.CharField(
		label='',
		max_length=30,
		required=False,
		widget=forms.HiddenInput(
			attrs={
				"display": "none"
			}
		)
	)

	phone_number = forms.CharField(
		label='Phone Number',
		max_length=17,
		min_length=9,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "+1xxxxxxxxx",
				"class": "form-control"
			}
		)
	)

	address_1 = forms.CharField(
		label='Address line 1',
		max_length=128,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "1000 Chastain Rd NW, Kennesaw",
				"class": "form-control"
			}
		)
	)

	address_2 = forms.CharField(
		label='Address line 2',
		max_length=128,
		widget=forms.TextInput(
			attrs={
				"placeholder": "apt#",
				"class": "form-control"
			}
		)
	)
	
	state = forms.ChoiceField(label='State', choices=STATE_CHOICES)
	
	zip_code = forms.CharField(
		label='Zip Code',
		max_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "30144",
				"class": "form-control"
			}
		)
	)

	county = forms.CharField(
		label='County',
		max_length=128,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Cobb County",
				"class": "form-control"
			}
		)
	)

	country = CountryField(blank_label='(Select country)').formfield()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'address_1', 'address_2', 'state', 'zip_code', 'county', 'country')

class OfficialSignUpForm(UserCreationForm):
	username = forms.CharField(
		label='Username',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "username",
				"class": "form-control"
			}
		)
	)

	email = forms.EmailField(
		label='Email',
		max_length=255,
		required=True,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "email@kennesaw.edu",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "••••••••",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "••••••••",
				"class": "form-control"
			}
		)
	)

	location = forms.CharField(
		label='',
		max_length=30,
		required=False,
		widget=forms.HiddenInput(
			attrs={
				"display": "none"
			}
		)
	)

	phone_number = forms.CharField(
		label='Phone Number',
		max_length=17,
		min_length=9,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "+1xxxxxxxxx",
				"class": "form-control"
			}
		)
	)

	organization = forms.CharField(
		label='Organization',
		max_length=128,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Organization",
				"class": "form-control"
			}
		)
	)

	address_1 = forms.CharField(
		label='Address line 1',
		max_length=128,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "1000 Chastain Rd NW, Kennesaw",
				"class": "form-control"
			}
		)
	)

	address_2 = forms.CharField(
		label='Address line 2',
		max_length=128,
		widget=forms.TextInput(
			attrs={
				"placeholder": "apt#",
				"class": "form-control"
			}
		)
	)
	
	state = forms.ChoiceField(label='State', choices=STATE_CHOICES)
	
	zip_code = forms.CharField(
		label='Zip Code',
		max_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "30144",
				"class": "form-control"
			}
		)
	)

	county = forms.CharField(
		label='County',
		max_length=128,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Cobb County",
				"class": "form-control"
			}
		)
	)

	country = CountryField(blank_label='(Select country)').formfield()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'organization', 'address_1', 'address_2', 'state', 'zip_code', 'county', 'country')