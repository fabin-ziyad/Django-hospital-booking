from django.contrib import admin
from . models import Contact, Department,Doctor,Booking
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
class showadmin(admin.ModelAdmin):
    list_display=('id','First_Name','Last_Name','Form_email','Phone_number','Messages','Messaged_On')
    search_fields=['id','First_Name','Last_Name','Form_email','Phone_number','Messages','Messaged_On']
admin.site.register(Contact,showadmin)
class BookinAdmin(admin.ModelAdmin):
    list_display=('id','patient_name','patient_phone','patient_email','Doc_name','patient_address','gender','book_time','Booking_Date','Booked_On')
    search_fields=['patient_name','patient_phone','patient_email','patient_address','gender','book_time','Booking_Date','Booked_On']
admin.site.register(Booking,BookinAdmin)






