from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BvisaAddForm#,RawBvisaForm
from .models import Bvisa

import smtplib
 
# def bvisa_add_view(request, *args, **kwargs):
# 	form = RawBvisaForm(request.GET)
# 	context= {"form":form}
# 	if request.method=="POST":
# 		form = RawBvisaForm(request.POST)
# 		context ={"form":form}
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			Bvisa.objects.create(**form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	return render (request,'bvisa/bvisa_add.html',context)

# def bvisa_add_view(request, *args, **kwargs):
# 	context ={}
# 	if request.method=="POST":
# 		emp_name =request.POST.get("employee_name")
# 		print(emp_name)
# 		#Bvisa.objects.create(employee_name=emp_name)
# 	return render (request,'bvisa/bvisa_add.html',context)

def send_mail(data):
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login('rsakthivinoth@gmail.com','******')
	server.sendmail("rsakthivinoth@gmail.com","rsakthivinoth@gmail.com", data)
	server.quit()

def bvisa_add_view(request, *args, **kwargs):
	if request.method =='POST':
	    form = BvisaAddForm(request.POST or None)
	    if form.is_valid():
		    form.save()
		    clean = form.cleaned_data
		
		    #send_mail(str(clean))
		    return redirect('../')
	    context ={'form':form}
	else:
		form = BvisaAddForm()
		context = {'form':form}
	return render (request,'bvisa/bvisa_add.html',context)

# Create your views here.
def bvisa_view(request,*args, **kwargs):
	
	context = {}
	return render (request, "bvisa.html",context)


def bvisa_detail_view(request, *args, **kwargs):
	obj = Bvisa.objects.get(id=1)
	context ={'object':obj}
	return render (request,'bvisa/bvisa_detail.html',context)