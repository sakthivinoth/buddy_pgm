from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import GCPAddForm#,RawGCPForm
from .models import GCP

import smtplib
 
# def GCP_add_view(request, *args, **kwargs):
# 	form = RawGCPForm(request.GET)
# 	context= {"form":form}
# 	if request.method=="POST":
# 		form = RawGCPForm(request.POST)
# 		context ={"form":form}
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			GCP.objects.create(**form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	return render (request,'GCP/GCP_add.html',context)

# def GCP_add_view(request, *args, **kwargs):
# 	context ={}
# 	if request.method=="POST":
# 		emp_name =request.POST.get("employee_name")
# 		print(emp_name)
# 		#GCP.objects.create(employee_name=emp_name)
# 	return render (request,'GCP/GCP_add.html',context)

def send_mail(data):
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login('rsakthivinoth@gmail.com','******')
	server.sendmail("rsakthivinoth@gmail.com","rsakthivinoth@gmail.com", data)
	server.quit()

def GCP_add_view(request, *args, **kwargs):
	if request.method =='POST':
	    form = GCPAddForm(request.POST or None)
	    if form.is_valid():
		    form.save()
		    clean = form.cleaned_data
		
		    #send_mail(str(clean))
		    return redirect('../')
	    context ={'form':form}
	else:
		form = GCPAddForm()
		context = {'form':form}
	return render (request,'gcp/gcp_add.html',context)

# Create your views here.
def GCP_view(request,*args, **kwargs):
	
	context = {}
	return render (request, "GCP.html",context)


def GCP_detail_view(request, *args, **kwargs):
	obj = GCP.objects.get(id=1)
	context ={'object':obj}
	return render (request,'GCP/GCP_detail.html',context)