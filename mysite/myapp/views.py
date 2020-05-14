from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from . import models
from . import forms
import json
import operator
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect("/login/")

def index(request):
    property_objects = models.Property_Model.objects.all()
    property_list=[]
    for prop in property_objects:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def priceOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('price')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def sqftOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('sq_footage')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def bedOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('num_rooms')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def bathOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('num_bathrooms')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def aptOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('type')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

def houseOrder(request):
    property_objects = models.Property_Model.objects.all()
    ordered_properties = property_objects.order_by('-type')
    property_list=[]
    for prop in ordered_properties:
        temp_prop = {}
        if prop.type == "A":
            temp_prop["type"]= "Apartment"
        else:
            temp_prop["type"]= "House"
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]= "$" + str(prop.price)
        if prop.upload == None:
            temp_prop["upload"] = ""
        else:
            temp_prop["upload"] = prop.upload.url
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
    }
    return render(request, "index.html", context=context)

@login_required
def addproperty(request):
    if request.method == "POST":
        if request.user.is_authenticated: #Must be logged in user to post
            form = forms.PropertyForm(request.POST, request.FILES) #request.files added
            if form.is_valid():
                form.save(request)
                return redirect("/")
        else:
            form = forms.PropertyForm()
    else:
        form = forms.PropertyForm()
    property_objects = models.Property_Model.objects.all()
    property_list=[]
    for prop in property_objects:
        temp_prop = {}
        temp_prop["type"]=prop.type
        temp_prop["address"]=prop.address
        temp_prop["num_rooms"]=prop.num_rooms
        temp_prop["num_bathrooms"]=prop.num_bathrooms
        temp_prop["sq_footage"]=prop.sq_footage
        temp_prop["price"]=prop.price
        temp_prop["upload"]=prop.upload
        property_list+=[temp_prop]

    context = {
        "title":"Final Project",
        "property_list":property_list,
        "form":form
    }
    return render(request, "addproperty.html", context=context)

@login_required
def applyproperty(request):
    if request.method == "POST":
        if request.user.is_authenticated: #Must be logged in user to post
            form = forms.ApplyForm(request.POST)
            if form.is_valid():
                form.save(request)
                return redirect("/")
        else:
            form = forms.ApplyForm()
    else:
        form = forms.ApplyForm()
    applicaton_objects = models.Application_Model.objects.all()
    application_list=[]
    for app in applicaton_objects:
        temp_app = {}
        temp_app["fname"]=app.fname
        temp_app["lname"]=app.lname
        temp_app["cur_address"]=app.cur_address
        temp_app["salary"]=app.salary
        temp_app["ssn"]=app.ssn
        temp_app["phone"]=app.phone
        application_list+=[temp_app]

    context = {
        "title":"Final Project",
        "application_list":application_list,
        "form":form
    }
    return render(request, "apply.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def chatindex(request):
    return render(request, 'chatindex.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
