from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import BvisaAddForm
from .models import Bvisa

import smtplib
from django.contrib import messages

def send_mail(employee_name, enterprise_id, project, no, start_date, end_date,cap):
	print("sending mail")
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login('rsakthivinoth@gmail.com','Windows@123')
	data = "Subject: Notification- New 710 Resource. Please assign a buddy !!\n Hey Admins, Please find the below Resource \n\nEmployee name = "+str(employee_name)+"\nEnterprise Id = "+str(enterprise_id)+"\nProject = "+str(project)+"\nContact number = "+str(no)+"\nTravel Start date = "+str(start_date)+"\nTravel end date = "+str(end_date)+"\nCapability = "+str(cap)+"\n\n\t **** This is a System generated mail. Please do not reply **** \n"
	server.sendmail("rsakthivinoth@gmail.com","rsakthivinoth@gmail.com", data)
	server.quit()

def bvisa_add_view(request, *args, **kwargs):
	if request.method =='POST':
	    form = BvisaAddForm(request.POST or None)
	    if form.is_valid():
		    form.save()
		    clean = form.cleaned_data
		    if clean:
		        send_mail(clean['employee_name'], clean['enterprise_id'], clean['project'],clean['whatsapp_number'],clean['travel_start_date'],clean['travel_end_date'],clean['capability'])
		        context ={'form':form}
		        messages.success(request, 'Form validation successful.Thanks you!!')
		        return HttpResponseRedirect('')
	    else:
	    	messages.warning(request, 'Form submission is not successful. Please retry with valid values')
	    	return HttpResponseRedirect('')
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