from django.shortcuts import render,redirect
from backend.models import *
from django.http import HttpResponse 
from django.contrib import messages
# Create your views here.

#-------------LOGICS FOR HOMEPAGES----------------#
# def manage_card(request):
#      return render(request,"Homepages/manageCard.html")
#----------Topbar----------#
def topbar(request):
    topbar_data=topbar_DB.objects.filter(status=True)
    if request.method == "POST":
        email=request.POST['email']
        mobile = request.POST['mob']
        address = request.POST['address']
        if topbar_DB.objects.filter(email=email,mobile=mobile,address=address).exists():
            return HttpResponse("you have already Added")
        else:
            topbar_DB.objects.create(email=email,mobile=mobile,address=address)
            return HttpResponse('You have Succesfully Added...')
    return render(request,'Homepages/manageTopbar.html',{"topbar_data":topbar_data})
#-----------Manage card for homePage----------#
def service_card(request):
    card_data=service_card_DB.objects.filter(status=True)
    if request.method =="POST":
        card_title=request.POST['title']
        card_description=request.POST['description']
        card_img=request.FILES['img']
        if service_card_DB.objects.filter(card_title=card_title,card_description=card_description,card_img=card_img).exists():
            return HttpResponse("you have already Added")
        else:
            service_card_DB.objects.create(card_title=card_title,card_description=card_description,card_img=card_img)
            return HttpResponse('you have Succesfully Added.....')
    return render(request,'Homepages/manageCard.html',{"card_data":card_data})    





#----------INDEX------------#
def homeVw(request):
        return render(request,"login.html")
def dashVw(request):
    if "email" in request.session:
        email = request.session['email']
        data=Registration_DB.objects.filter(email=email).first()
        return render(request,'dash.html',{'data':data})
    else:
        return redirect('backend/login')
    return render(request,'backend/dash.html')
def adduser(request):
    return render(request,'adduser.html')
def viewuser(request):
    return render(request,'viewuser.html')
def addcustomer(request):
    return render(request,'addcustomer.html')
def viewcustomer(request):
    return render(request,'viewcustomer.html')

#----------LOGIN------------#
def Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]
        if Registration_DB.objects.filter(email=email,password=password).exists():
            request.session['email']=email
            return redirect("/backend/dash")
        else:
            messages.info(request,"invalid email/password")
            return redirect('/backend/login')
            # return HttpResponse('your Email/Password is invalid')
    return render(request,'login.html')

def authen(request):
    if('email') in request.session:
        return redirect('/dash')
    else:
        return redirect('/')
def Logout(request):
    del request.session['email']
    messages.info(request,"Logout Succesfully.....")
    return redirect('/')
#--------Registration-----------------#
def RegistrationVw(request):
    if request.method == "POST":
        name=request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        if Registration_DB.objects.filter(name=name,email=email,password=password).exists():
            return HttpResponse("you have already Registered")
        else:
            Registration_DB.objects.create(name=name,email=email,password=password)
            return HttpResponse('You have Succesfully Registered...')
    return render(request,'adduser.html')

#---------get user----------#
def userlist(request):
    user_data=Registration_DB.objects.filter(status=True)
    return render(request,"viewuser.html",{"user_data":user_data})
#.......//////// userlist   [Update] \\\\\\\\\.........# 
def Updt_User_List(request,id):
    if "email" in request.session:
        email = request.session['email']
        data=Registration_DB.objects.filter(email=email).first()
        user_data=Registration_DB.objects.filter(id=id)
        if request.method=="POST":
            name=request.POST['name']
            email = request.POST['email']
            password = request.POST['pass']
            Registration_DB.objects.filter(id=id).update(name=name,email=email,password=password)
            messages.info(request,name+' '+'Updated Successfully...!!#')
            return redirect('/adduser')
        return render(request,'updateuser.html',{"user_data":user_data,"data":data})
    else:
        return redirect('/')   
#----------CUSTOMER LIST-----------#
def cus_list(request):
    list=customer_DB.objects.filter(status=True)
    return render(request,"viewcustomer.html",{"list":list})
#----------Delete user----------#
def Delete_user(request,id):
     Registration_DB.objects.filter(id=id).update(status=False)
     return redirect('viewuser')

#----------Delete customer----------#
def Delete_customer(request,id):
     customer_DB.objects.filter(id=id).update(status=False)
     return redirect('/viewcustomer')
#--------- CUSTOMER LIST UPDATES---------#
def updates_cus_list(request,id):
    cus_data = customer_DB.objects.filter(id=id)
    return render(request,'cutomer_update.html',{"cus_data:cus_data"})
    if request.method == "POST":
        name = request.POST['cus_name']
        mobile = request.POST['cus_num']
        dob = request.POST['date']
        addr = request.POST['addr']
        service_type = request.POST['service_type']
        curr_date = request.POST['curr_date']
        image = request.FILES['img']
        application_no = request.POST['apl_num']
        user = request.POST['cus_user']
        remark = request.POST['remark']
        data = customer_DB.objects.get(id=id)
        if image.size == 0:
            data.name=name
            data.mobile=mobile
            data.dob=dob
            data.addr=addr
            data.service_type=service_type
            data.curr_date=curr_date
            data.application_no=application_no
            data.user=user
            data.remark=remark
            data.save()
        else:
            data.name=name
            data.mobile=mobile
            data.dob=dob
            data.addr=addr
            data.service_type=service_type
            data.curr_date=curr_date
            data.image=image
            data.application_no=application_no
            data.user=user
            data.remark=remark
            data.save()
        return redirect('/viewcustomer')
    return render(request,'viewcustomer.html',{"cus_data:cus_data"})
    
            
                



#------------ADD EMPLOYEE LIST--------#
def addcustomer(request):
    if "email" in request.session:
        email = request.session['email']
        data=Registration_DB.objects.filter(email=email).first()
        if request.method == "POST":
            name = request.POST['cus_name']
            mobile = request.POST['cus_num']
            dob = request.POST['date']
            addr = request.POST['addr']
            service_type = request.POST['service_type']
            curr_date = request.POST['curr_date']
            image = request.FILES['img']
            application_no = request.POST['apl_num']
            user = request.POST['cus_user']
            remark = request.POST['remark']
            if customer_DB.objects.filter(name=name,mobile=mobile,dob=dob,addr=addr,service_type=service_type,
                                      curr_date=curr_date,image=image,application_no=application_no,user=user,remark=remark).exists():
             return HttpResponse('employee data is already register')
            else:
                customer_DB.objects.create(name=name,mobile=mobile,dob=dob,addr=addr,service_type=service_type,
                                      curr_date=curr_date,image=image,application_no=application_no,user=user,remark=remark)
                return HttpResponse('data has been submitted successfully....')
        return render(request,'addcustomer.html',{'data':data})
    else:
        return redirect('/')
    
     

# Create your views here.

