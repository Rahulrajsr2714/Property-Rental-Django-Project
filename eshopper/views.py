from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from eshopper.models import Account,Property,PropertyImages
from django.http import HttpResponse , HttpResponseRedirect
from .forms import LoginForm,SignupForm,AddProperty
from django.contrib import messages

def login_account(request):
    if request.user.is_authenticated:
        #return HttpResponse('You are already logged in')
        return HttpResponseRedirect('listprprty')
    else:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        #return HttpResponse('Login Successful')
                        return HttpResponseRedirect('listprprty')
                    else:
                        return HttpResponse('Your account is not active')
                else:
                    return HttpResponse('The Account does not exists')
            else:
                login_form = LoginForm()
                return render(request, "login.html",{"form":LoginForm})
        else:
            login_form = LoginForm()
        return render(request, "login.html",{"form":LoginForm})
@login_required(login_url=login_account)
def logout_account(request):
    logout(request)
    return render(request,"login.html",{"form":LoginForm})

def homepage(request):
    return render(request,"index.html")
def menu(request):
    return render(request,"menu.html")


# def signup(request):
#     return render(request,"signup.html",{"form":SignupForm})


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            name = signup_form.cleaned_data['name']	
            username = signup_form.cleaned_data['username']	
            email = signup_form.cleaned_data['email']	
            phone = signup_form.cleaned_data['phone']
            password = signup_form.cleaned_data['password']	
            repassword = signup_form.cleaned_data['repassword']	
            if (password == repassword):
                if  Account.objects.filter(username=username).exists():
                    return HttpResponse("Username/Email Already Exists")
                else:	

                    user = Account.objects.create_user(email,username,phone,name,password)
                    user.save()
                    return HttpResponse("Signup successfull")
            else:
                return HttpResponse("Password didnt match")
    else:
        signup_form = SignupForm(request.POST)
    return render(request, 'signup.html',{"form":SignupForm})					
	
@login_required(login_url=login_account)
def addproperty(request):
    if request.method == 'POST':
        property_form = AddProperty(request.POST,request.FILES)
        ip_property_images = request.FILES.getlist('image_field')
        if property_form.is_valid():
            ip_property_name = property_form.cleaned_data['property_name'] 
            ip_property_description = property_form.cleaned_data['property_description'] 
            ip_property_rent = property_form.cleaned_data['property_rent']
            ip_property_address = property_form.cleaned_data['property_address']
            ip_property_landmark = property_form.cleaned_data['property_landmark']
            property_object = Property(property_name=ip_property_name,
                            property_description = ip_property_description,
                            property_rent = ip_property_rent,
                            property_address=ip_property_address,
                            property_landmark=ip_property_landmark,
                            property_holder = request.user)
            property_object.save() # will save the data from the form to database 
            for f in ip_property_images:
                property_image_object = PropertyImages(prop_id = property_object, 
                                        property_img = f,
                                        )
                property_image_object.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Added Your Property '+ip_property_name)
            return HttpResponseRedirect("listprprty")
        else:
            return HttpResponse("form invalid")
    else:
        property_form = AddProperty() 
        return render(request,"addproperty.html",{'form':property_form,})
 
def showImage(request):

    print("hiii")
    print("hii")
    img = PropertyImages.objects.filter(prop_id=11)
    print(img)
    return render(request, 'showimage.html', {"file":img})


def viewproperties(request):
    propertylist = Property.objects.all()
    propertyimagelist = PropertyImages.objects.distinct()
    if request.user.username is '' :
        users = 'Guest User'
    else:
        users = request.user.username     
    mylist = zip(propertylist,propertyimagelist)
    context = {"mylist": mylist,"username":users}
    return render(request,"list-properties.html",context)
    

     #pentaho
@login_required(login_url=login_account)
def myproperties(request):
    mypropertieslist = Property.objects.filter(property_holder=request.user)
    context = {"prprtylist":mypropertieslist}
    return render(request,"my-properties.html",context)

def viewdetails(request):
    imagelist = PropertyImages.objects.all()
    context = {"imglist":imagelist}
    return render(request,"view-details.html",context)

@login_required(login_url=login_account)
def deactiveproperty(request,prop_id):
    propertylist = Property.objects.get(id=prop_id)
    propertylist.property_available = 0
    propertylist.save()
    messages.add_message(request, messages.ERROR, 'Successfully removed '+propertylist.property_name+" From all Properties")
    return HttpResponseRedirect('/eshopper/myproperties')
    # return HttpResponse("Success")
    # return render(request,)

@login_required(login_url=login_account)
def activeproperty(request,prop_id):
    propertylist = Property.objects.get(id=prop_id)
    propertylist.property_available = 1
    propertylist.save()
    messages.add_message(request, messages.SUCCESS, 'Successfully Listed  '+propertylist.property_name+" On all Properties")
    return HttpResponseRedirect('/eshopper/myproperties')