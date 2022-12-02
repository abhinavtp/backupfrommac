
from django.shortcuts import render,redirect
from app.models import Registration, product,Doctor
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app.serializers import DoctorRegSerializers
from decorators import login_check
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def baabtra(request):
    return render(request, 'the/baabtra.html')
def blog(request):
    return render(request,'the/blog.html')

def aboutus(request):
    return render(request,'the/aboutus.html')
def placement(request):
    return render(request,'the/placement.html')      
def anwer(request):
    return render(request,'the/anwer.html')  

def new(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone= request.POST['phone']
        password = request.POST['password']
        photo = request.FILES['photo']
        # profile_images = str(random())+photo.name
        # add_images = FileSystemStorage()
        # add_images.save(profile_images, photo)

        userobj = Registration(name=name,email=email,phone=phone,password=password,photo=photo)
        userobj.save()

        request.session['userid'] = userobj.id
        subject = "welcome to my app "
        message = 'hi {userobj.name}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [userobj.email]
        try:
            send_mail(subject,message,email_from,recipient_list)
        except Exception as e:
            print(e)    
        


 
    return render(request,'the/new.html')    


def db(request):
    userdata = Registration.objects.all()
    return render(request,'the/db.html',{'data': userdata})    

def login(request):
    if 'userid' not in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Registration.objects.get(email=email,password=password)
                # if user.email == email and user.password == password :
                request.session['userid'] = user.id
                print(request.session['userid'])
                return redirect('hom')
            except: 
                return render(request,'the/login.html',{'errormsg':'invalid email or password'})

    

        return render(request,'the/login.html')
    return redirect('pro')    
    

@login_check
def profile(request):
        # if 'userid' in request.session: 
        current_user = Registration.objects.get(id = request.session['userid'])
        #     return render(request,'the/profile.html',{'name':current_user})   
        # return redirect('lo')     
        return render(request,'the/profile.html')   



def logout(request):
    del request.session['userid']
    return redirect('lo')    


def addproduct(request):
    if request.method == "POST":
        name = request.POST['name']
        discription = request.POST['discription']
        price = request.POST['price']
        quantity = request.POST['quantity']
        category = request.POST['category']
        user = request.session['userid']
        userobj = product(name=name, discription=discription, price=price, quantity=quantity, catagory=category, user_id=user)
        userobj.save()

    return render(request,'the/addproduct.html')

def home(request):
    return render(request,'the/home.html')        

def view_products(request):
    productobj = product.objects.filter(user_id = request.session['userid'])
    return render(request, 'the/view_products.html',{'data':productobj})   


def updateproduct(request, id=0):
    print(id)
    
    productobj = product.objects.get(id = id)
    return render(request,'the/updateproduct.html',{'product':productobj})

def delete(request, id=0):
    productobj = product.objects.get(id=id).delete()
    return redirect ('view')


@csrf_exempt
def emailcheck(request):
    email=request.POST.get('email')
    print(email)
    email_exist = Registration.objects.filter(email=email).exists()
    print(email_exist)

    return  JsonResponse({"message":email_exist})


def insert(request):
    return render(request,'the/insert')    

def insertcheck(request):
    return ()       


@csrf_exempt
def serve_doctors(request, id=0):

    if request.method == "POST":
        doctordata = JSONParser().parse(request)
        print(doctordata)
        doctor_serializer = DoctorRegSerializers(data = doctordata)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return  JsonResponse({"status" : "doctor registerd successfully"})

    elif request.method == "GET":
        doctor = Doctor.objects.all()    
        doctor_serializer = DoctorRegSerializers(doctor,many = True)
        return JsonResponse({"data" : doctor_serializer.data})

    elif request.method == "PUT":
        doctordata = JSONParser().parse(request)  
        doctor = Doctor.objects.get(id = doctordata ['id'])  
        doctor_serializer = DoctorRegSerializers(doctor,doctordata)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse({" status" : "data updated successfully"})

    
    elif request.method == "DELETE":
        doctor = Doctor.objects.get (id = id)
        doctor.delete()
        return JsonResponse({})
  
    return  JsonResponse({'status':'registration faild'})


