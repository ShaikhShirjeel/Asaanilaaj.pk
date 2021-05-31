from django.contrib import admin
from hospitals.models import *

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Payment_Method)
admin.site.register(Bills)
admin.site.register(Record_Details)
admin.site.register(Appointment)
admin.site.register(time_slots)

# class DoctorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Doctor, DoctorAdmin)

# class PatientAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Patient, PatientAdmin)

# class AppointmentAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Appointment, AppointmentAdmin)

# class PatientDischargeDetailsAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)