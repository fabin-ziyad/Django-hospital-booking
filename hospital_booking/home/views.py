from email.message import Message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Department, Doctor, Booking, Contact
from .forms import CreateUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
########################################################################################################
#  REGISTER USER


def register_request(request):
    form = CreateUserForm()
    user = request.POST.get('username')
    # name=request.POST.get('first_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 != password2:
        messages.error(request, 'password doesnt match')
        return redirect('register')

    check_user = User.objects.filter(first_name=user).first()
    if check_user is not None:
        messages.error(request, 'username exists')
        return redirect('register')

    check_email = User.objects.filter(email=email).first()
    if check_email is not None:
        messages.error(request, 'email exists')
        return redirect('register')
    # check_name=User.objects.filter(first_name=name).first()
    # if check_name is not None:
    #      messages.error(request,'This name exists')
    #      return redirect('register')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'register.html', context)


########################################################################################################
#  LOGIN USER

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'signin.html', context)


########################################################################################################
#  LOGOUT USER
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


########################################################################################################
#   HOME

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


########################################################################################################
#   BOOKING

@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_email = request.POST.get('email')
        patient_phone = request.POST.get('phone')
        patient_address = request.POST.get('address')
        doc_name = Doctor.objects.get(Doc_name=request.POST.get('doctor'))
        Booking_date = request.POST.get('date')
        book_time = request.POST.get('time')
        Gender = request.POST.get('gender')
        Booking(patient_name=patient_name, patient_phone=patient_phone, patient_email=patient_email, patient_address=patient_address,
                Doc_name=doc_name, Booking_Date=Booking_date, book_time=book_time, gender=Gender).save()
        bookLatest=Booking.objects.latest('patient_phone')
        bookLatest_dict={
            'patients':bookLatest.patient_name,
            'patients_phone':bookLatest.patient_phone,
            'patients_email':bookLatest.patient_email,
            'patients_address':bookLatest.patient_address,
            'Doctor_booked':bookLatest.Doc_name,
            'Booking_date':bookLatest.Booking_Date,
            'book_time':bookLatest.book_time,
            'gender':bookLatest.gender
        }
        patient_number=bookLatest_dict['patients_phone']
        print(patient_number)

        # print(bookLatest_dict['gender'])
        # return redirect('home')
    dict_book=Booking.objects.filter().order_by('-id')[:7:0]
    dict_form = Doctor.objects.all()
    
    
    return render(request, 'booking.html', {'form':dict_form,'bookings':dict_book})


#######################################################################################################
#  ABOUT

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


#######################################################################################################
#  DOCTORS

@login_required(login_url='login')
def doctors(request):
    dict_doctors = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'doctors.html', dict_doctors)


########################################################################################################
#  CONTACT

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        Firstname = request.POST.get('FirstName')
        Lastname = request.POST.get('LastName')
        Form_email = request.POST.get('FormEmail')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact(First_Name=Firstname, Last_Name=Lastname, Phone_number=phone,
                Messages=message, Form_email=Form_email).save()
        dic_Contact = Contact.objects.latest('id')
        subject = "website"
        dict_one = {
            'firstname': dic_Contact.First_Name,
            'lastname': dic_Contact.Last_Name,
            'email': dic_Contact.Form_email,
            'phonenumber': dic_Contact.Phone_number,
            'Message': dic_Contact.Messages
        }
        list_dict=list(dict_one.items())
        print(list_dict)
        print(list_dict[2])
        print(dict_one)
        print(dict_one['email'])
        # send_mail(subject,message, settings.EMAIL_HOST_USER, ['hubdigital9@gmail.com'], fail_silently=False)
        # # messages.success(request, 'Success!')
        return redirect ('home')   
    return render( request, 'contact.html',{'form':Contact})

############################################################
#         subject='website'                                #
#         from_mail=settings.EMAIL_HOST_USER               #
#         to_email=[from_mail,'hubdigital9@gmail.com']     #
#         contact_message = ('firstname','Message')        #
#         send_mail(                                       #
#     subject,                                             #
#     contact_message,                                     #
#     from_mail,                                           #
#     to_email,                                            #
#     fail_silently=False, )                               #
############################################################

########################################################################################################
#  DEPARTMENT

@login_required(login_url='login')
def department(request):
    dict_dept = {
        'departments': Department.objects.all()
    }
    return render(request, 'department.html', dict_dept)


#######################################################################################################
