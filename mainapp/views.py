from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import *
import random


def index(request):
    return HttpResponse('Hello welcome in main app')

def farmer_signup(request):
    if request.method != 'POST':
        pass
    else:
        global farmer_first_name, farmer_last_name, farmer_contact_no,farmer_email, farmer_password
        farmer_first_name = request.POST.get('first_name')
        farmer_last_name = request.POST.get('last_name')
        farmer_contact_no = request.POST.get('contact_no')
        farmer_email = request.POST.get('email')
        farmer_password = request.POST.get('password')
        farmer_re_password = request.POST.get('re-password')
        
        correct_info = 'YES'

        if not (farmer_first_name.isalpha()):
            messages.error(request, 'First name must be alphabetic ')
            correct_info = 'NO'

        if not (farmer_last_name.isalpha()):
            messages.error(request, 'Last name must be alphabetic ')
            correct_info = 'NO'

        if len(farmer_contact_no) != 10 :
            messages.error(request, 'Contact no should be equal to 10')
            correct_info = 'NO'

        if len(farmer_password) < 8:
            messages.error(request, 'your password length should be more than 8')   
            correct_info = 'NO'


        elif farmer_password != farmer_re_password:
            messages.error(request, "Password does not match")
            correct_info = 'NO'

        if(correct_info == 'YES'):
            random1 = random.randint(1000, 9999)
            request.session['random1'] = random1

            send_mail(
            'mandi bazar',
            f'Your OTP for register with mandi-bazar is :{random1}',
            settings.EMAIL_HOST_USER, 
            [farmer_email],
            fail_silently=False,
            )
            return HttpResponseRedirect('/mandi/farmer_otp')

        else:
            print('Incorrect info')
    return render(request, 'farmer_signup.html')

def farmer_confirm_otp(request):
    if request.method != 'POST':
        pass
    else:
        user_otp = request.POST.get('otp')
        print(user_otp)
        
        random1 = request.session.get('random1')

        print(random1)
        if(random1 == int(user_otp)):
            print('Register Successfully')
            
            farmer = Farmers_detail()
            farmer.full_name = farmer_first_name + " " + farmer_last_name
            farmer.contact_no = farmer_contact_no
            farmer.email = farmer_email
            farmer.password = farmer_password
            farmer.save()

            return HttpResponseRedirect('/mandi/farmer-login')

        else:
            print('not match')
    
    return render(request, 'farmer_otp.html')

def farmer_login(request):
    if request.method != 'POST':
        pass
    else:
        user_email = request.POST.get('email')
        user_password =  request.POST.get('password')
        print(user_email)
        print(user_password)

        queryset = Farmers_detail.objects.filter(email= user_email, password=user_password)
        list(queryset)
        if(len(queryset) !=0):    
            print('loged in successfully')
            request.session['email'] = user_email
            return HttpResponseRedirect('/mandi/farmer_home')
        else:
            messages.error(request, 'Email and password does not match')    
    return render(request, 'farmer_login.html')

def farmer_home(request):
    email = request.session.get('email')
    
    return render(request, 'farmer_home.html',{"email":email})

def farmer_complete_profile(request):
    if request.method != 'POST':
        pass
    else:
        email = request.session.get('email')

        farmer_Adhar_card = request.POST.get('Adhar_card')
        farmer_pan_card = request.POST.get('Pan_card')
        farmer_address = request.POST.get('Address')
        farmer_bank_account_no = request.POST.get('Bank_account_no')
        farmer_account_holder_name = request.POST.get('Account_holder_name')
        farmer_ifsc_code = request.POST.get('Ifsc_code')

        farmer_account_holder_name2 = farmer_account_holder_name.replace(" ", "")        
        correct_info = 'YES'

        if len(farmer_Adhar_card) != 12:       
            messages.error(request, 'please enter correct adhar card number')
            correct_info = 'NO'

        if len(farmer_pan_card) != 10:       
            messages.error(request, 'please enter correct pan card number')
            correct_info = 'NO'

        if not (farmer_account_holder_name2.isalpha()):
            messages.error(request, 'User name must be alphabetic ')
            correct_info = 'NO'

        if(correct_info == 'YES'):

            farmer = Farmers_detail.objects.get(email=email)
            farmer.adhar_card = farmer_Adhar_card
            farmer.pan_card = farmer_pan_card
            farmer.address = farmer_address
            farmer.bank_account_no = farmer_bank_account_no
            farmer.account_holder_name = farmer_account_holder_name
            farmer.ifsc_code = farmer_ifsc_code
            farmer.save() 

    return render(request, "farmer_complete_profile.html")

def product_form(request):
    if request.method != 'POST' and ('image1' not in request.FILES and 'image2' not in request.FILES and 'video' not in request.FILES):
        pass
    else:
        print('hy')
        print('hy')
        product_name = request.POST.get("product_name")
        product_subtype = request.POST.get("subtype")
        quantity = request.POST.get("quantity")
        district = request.POST.get("district")
        base_price = request.POST.get("base_price")
        description = request.POST.get("description")
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        video = request.FILES.get('video')
        
        email = request.session.get('email')
        queryset = Farmers_detail.objects.filter(email=email)
        list(queryset)
        id = queryset[0].id


        product = Product_details()
        product.product_type = product_name
        product.subtype = product_subtype
        product.quantity = quantity
        product.district_name = district
        product.base_price = base_price
        product.description = description
        product.product_image1 = image1
        product.product_image2 = image2
        product.product_video = video
        product.farmer_id = id
        product.save()

    return render(request, 'product_form_page.html')

def businessman_signup(request):
    if request.method != 'POST':
        pass
    else:
        global businessman_first_name, businessman_last_name, businessman_contact_no,businessman_email, businessman_password
        businessman_first_name = request.POST.get('first_name')
        businessman_last_name = request.POST.get('last_name')
        businessman_contact_no = request.POST.get('contact_no')
        businessman_email = request.POST.get('email')
        businessman_password = request.POST.get('password')
        businessman_re_password = request.POST.get('re-password')
        
        correct_info = 'YES'

        if not (businessman_first_name.isalpha()):
            messages.error(request, 'First name must be alphabetic ')
            correct_info = 'NO'

        if not (businessman_last_name.isalpha()):
            messages.error(request, 'Last name must be alphabetic ')
            correct_info = 'NO'

        if len(businessman_contact_no) != 10 :
            messages.error(request, 'Contact no should be equal to 10')
            correct_info = 'NO'

        if len(businessman_password) < 8:
            messages.error(request, 'your password length should be more than 8')   
            correct_info = 'NO'


        elif businessman_password != businessman_re_password:
            messages.error(request, "Password does not match")
            correct_info = 'NO'

        if(correct_info == 'YES'):
            random2 = random.randint(1000, 9999)
            request.session['random2'] = random2
            print(random2)
            send_mail(
            'mandi bazar',
            f'Your OTP for register with mandi-bazar is :{random2}',
            settings.EMAIL_HOST_USER, 
            [businessman_email],
            fail_silently=False,
            )
            return HttpResponseRedirect('/mandi/businessman_otp')

        else:
            print('Incorrect info')

    return render(request, 'businessman_signup.html')

def businessman_confirm_otp(request):

    if request.method != 'POST':
        pass
    else:
        user_otp = request.POST.get('otp')
        print(user_otp)
        
        random2 = request.session.get("random2")

        print(random2)
        if(random2 == int(user_otp)):
            print('Register Successfully')
            
            businessman = Businessman_details()
            businessman.full_name = businessman_first_name + " " + businessman_last_name
            businessman.contact_no = businessman_contact_no
            businessman.email = businessman_email
            businessman.password = businessman_password
            businessman.save()

            return HttpResponseRedirect('/mandi/businessman-login')

        else:
            print('not match')
    
    return render(request, 'businessman_otp.html')


def businessman_login(request):
    if request.method != 'POST':
        pass
    else:
        user_email = request.POST.get('email')
        user_password =  request.POST.get('password')
        print(user_email)
        print(user_password)

        queryset = Businessman_details.objects.filter(email= user_email, password=user_password)
        list(queryset)
        if(len(queryset) !=0):    
            print('loged in successfully')
            request.session['email2'] = user_email
            return HttpResponseRedirect('/mandi/businessman_home')
        else:
            messages.error(request, 'Email and password does not match')    
    return render(request, 'businessman_login.html')


