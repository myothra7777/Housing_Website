from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
    return value

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user)>0:
        raise forms.ValidationError("Email Already Exists")
    return value

def must_be_bob(value):
    if not value.startswith("BOB"):
        raise forms.ValidationError("Must be BOB")
    return value

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
        )

    first_name = forms.CharField(
        label="First Name",
        required=True,
        )

    last_name = forms.CharField(
        label="Last Name",
        required=True,
        )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class PropertyForm(forms.Form):
    type = forms.ChoiceField(choices=models.property_types, label="Property Type")
    address = forms.CharField(max_length=100, label="Address")
    num_rooms = forms.CharField(max_length=2, label="Number of Bedrooms")
    num_bathrooms = forms.CharField(max_length=2, label="Number of Bathrooms")
    sq_footage = forms.CharField(max_length=5, label="Square Footage")
    price = forms.CharField(max_length=20, label="Monthly Cost")
    upload = forms.ImageField(label="Upload")

    def save(self, request):
        property_instance = models.Property_Model()
        property_instance.type = self.cleaned_data["type"]
        property_instance.address = self.cleaned_data["address"]
        property_instance.num_rooms = self.cleaned_data["num_rooms"]
        property_instance.num_bathrooms = self.cleaned_data["num_bathrooms"]
        property_instance.sq_footage = self.cleaned_data["sq_footage"]
        property_instance.price = self.cleaned_data["price"]
        property_instance.upload = self.cleaned_data["upload"]
        property_instance.save()
        return property_instance

class ApplyForm(forms.Form):
    fname = forms.CharField(max_length=50, label="First Name")
    lname = forms.CharField(max_length=50, label="Last Name")
    cur_address = forms.CharField(max_length=100, label="Current Address")
    salary = forms.CharField(max_length=10, label="Monthly Salary")
    ssn = forms.CharField(max_length=11, label="SSN")
    phone = forms.CharField(max_length=20, label="Phone Number")

    def save(self, request, prop_id):
        property_instance = models.Property_Model.objects.filter(id=prop_id).get()
        application_instance = models.Application_Model()
        application_instance.property = property_instance
        application_instance.applicant = request.user
        application_instance.fname = self.cleaned_data["fname"]
        application_instance.lname = self.cleaned_data["lname"]
        application_instance.cur_address = self.cleaned_data["cur_address"]
        application_instance.salary = self.cleaned_data["salary"]
        application_instance.ssn = self.cleaned_data["ssn"]
        application_instance.phone = self.cleaned_data["phone"]
        application_instance.save()
        return application_instance
