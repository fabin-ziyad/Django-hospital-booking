from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('booking/',views.booking, name='booking'),
    path('doctors/',views.doctors, name='doctors'),
    path('contact/',views.contact, name='contact'),
    path('department/',views.department, name='department'), 
    # path('signin/',views.signin,name='signin'),
    # path('signup/',views.signup,name='signup'),
     path('register', views.register_request, name="register"),
     path('login', views.login_request, name="login"), 
     path('logout', views.logoutUser, name="logout") 

]
    