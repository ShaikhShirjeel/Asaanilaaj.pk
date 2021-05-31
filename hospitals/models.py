from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class DoctorRating(models.Model):
    rating = models.FloatField()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    dob = models.DateField(max_length=20)
    contact_no = models.CharField(max_length=20,null=False)
    patient_address = models.CharField(max_length=40)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    #profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    #symptoms = models.CharField(max_length=100,null=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

    
class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name
    

class Doctor(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    dob = models.DateField(max_length=20)
    doj = models.DateField(max_length=20)
    contact_no = models.CharField(max_length=20, null= True)
    qualification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    timing = models.TextField(max_length=20)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)  
    status=models.BooleanField(default=False)
    meet_link= models.URLField(max_length=100)
    #profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.dept)


    def __str__(self):
        return self.user.first_name + self.user.last_name

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dept = models.ManyToManyField(Department, blank=True)
    doctor = models.ManyToManyField(Doctor, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    #profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)


class Record_Details(models.Model):
    patient_diagnoses = models.CharField(max_length=100)
    medicines = models.CharField(max_length=100)
    surgery = models.CharField(max_length=100)
    other_details = models.CharField(max_length=100)
    patient = models.OneToOneField(Patient, on_delete = models.CASCADE)

class Bills(models.Model):
    bill_date = models.DateTimeField(default=timezone.now)
    bill_amount = models.IntegerField()
 
class Payment_Method(models.Model):
    crd_card_no = models.IntegerField()
    dbt_card_no = models.IntegerField()
    payment_date = models.DateTimeField(default=timezone.now)
    payment_recv = models.IntegerField()
    payment_bal = models.IntegerField()
    bill = models.ForeignKey(Bills, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE)

class time_slots(models.Model):
    doctor_id=models.CharField(max_length=100)
    from_time=models.CharField(max_length=10)
    to_time=models.CharField(max_length=10)

    class Meta:
        db_table='time_slots'

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)


#when problem in running python manage.py migrate
#     python manage.py migrate --fake myappname zero
# This reset all migrations (to the zeroth state)

# This followed by :

# python manage.py migrate myappname
# created the tables for me.

# If you do not want to roll back to the initial(zero) state but say to the migration number 0005(the last migration that worked), you can instead do this:

# python manage.py migrate --fake myappname 0005
# And then proceed with the actual migrate:

# python manage.py migrate myappname