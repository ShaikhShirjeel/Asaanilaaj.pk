from django.contrib.auth import get_user_model
from django.db import transaction
from .models import *
from django import forms
#from django.contrib.auth.models import User
from . import models

UserModel = get_user_model()

class HospitalSignUpForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password1 = forms.CharField(
        label= "Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"user-password"
            }
        )
    )
    password2 = forms.CharField(
        label= "Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"user-confirm-password"
            }
        )
    )
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    # city = forms.CharField(required=True)
    # country = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This is an invalid Username. Pick another! ")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This is an invalid email. Pick another! ")
        return email

class PatientSignUpForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password1 = forms.CharField(
        label= "Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"user-password"
            }
        )
    )
    password2 = forms.CharField(
        label= "Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"user-confirm-password"
            }
        )
    )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    gender = forms.CharField(required=True)
    dob = forms.DateField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an invalid Username. Pick another! ")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This is an invalid email. Pick another! ")
        return email


 #  ************************** ******************* ***************** *************




#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','contact_no','dept','status','gender','city',
                'dob','doj','qualification','designation','country','timing','meet_link']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['patient_address','contact_no','status','gender','city','dob','country']



class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))