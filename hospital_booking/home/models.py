from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=70,default="")
    dep_discription=models.TextField()
    def __str__(self):
        return self.dep_name
class Doctor(models.Model):
    Doc_name=models.CharField(max_length=150)
    Doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    Doc_image=models.ImageField (upload_to='doctors')
    def __str__(self):
        return self.Doc_name + ' -   -(' + self.Doc_spec + ')'
    
class Booking(models.Model):
    patient_name=models.CharField(max_length=150,default="")
    patient_phone=models.CharField(max_length=10,default="")
    patient_email=models.EmailField(default="")
    patient_address=models.TextField(default="")
    Doc_name=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Booking_Date=models.DateField(default="")
    book_time=models.TimeField(default="",blank=True)
    gender=models.CharField(max_length=20,default='Male')
    Booked_On=models.DateField(auto_now=True)
    Booked_On_Time=models.DateTimeField( auto_now=True)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=200,blank=True,null=True)
    Last_Name=models.CharField(max_length=200,null=True)
    Form_email=models.CharField(max_length=300,null=True)
    Phone_number=models.CharField(max_length=12,null=True)
    Messages=models.CharField(max_length=400,blank=True,null=True)
    Messaged_On=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.FirstName + self.LastName

