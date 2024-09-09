from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    # path('Home',views.Home,name='Home'),
    # path('Features',views.Features,name='Features'),
    # path('Pricing',views.Pricing,name='Pricing'),
    # path('Contact',views.Contact,name='Contact'),
    # path('About',views.About,name='About'),
    # path('SIGN_IN',views.SIGN_IN,name='SIGN_IN'),
]