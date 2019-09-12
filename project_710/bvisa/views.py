from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from .forms import BvisaAddForm
from .models import Bvisa

import smtplib
from django.contrib import messages

def send_mail(employee_name, enterprise_id, project, no, start_date, end_date,cap):
	print("sending mail")
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login('rsakthivinoth@gmail.com','********')
	data = "Subject: Notification- New P710 Resource. Please assign a buddy !!\n Hey Admins, Please find the below Resource \n\nEmployee name = "+str(employee_name)+"\nEnterprise Id = "+str(enterprise_id)+"\nProject = "+str(project)+"\nContact number = "+str(no)+"\nTravel Start date = "+str(start_date)+"\nTravel end date = "+str(end_date)+"\nCapability = "+str(cap)+"\n\n\t **** This is a System generated mail. Please do not reply **** \n"
	server.sendmail("rsakthivinoth@gmail.com","rsakthivinoth@gmail.com", data)
	server.quit()

def send_succ_mail():
	print("sending mail")
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login('rsakthivinoth@gmail.com','********')
	data = "Subject: Notification - P710 Buddy portal \n Hi..\n Thanks for registering\nFor any queries. Please reach out to mail@accenture.com \n\n\n\t **** This is a System generated mail. Please do not reply **** \n"
	server.sendmail("rsakthivinoth@gmail.com","rsakthivinoth@gmail.com", data)
	server.quit()

def bvisa_add_view(request, *args, **kwargs):
	if request.method =='POST':
		form = BvisaAddForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			form.save()
			clean = form.cleaned_data
			if clean:
				print(clean['employee_name'], clean['enterprise_id'], clean['project'],clean['whatsapp_number'],clean['travel_start_date'],clean['travel_end_date'],clean['capability'])
				#send_mail(clean['employee_name'], clean['enterprise_id'], clean['project'],clean['whatsapp_number'],clean['travel_start_date'],clean['travel_end_date'],clean['capability'])
				#send_succ_mail()
				form = BvisaAddForm()
				context ={'form':form}
				messages.success(request, 'Form submission successful')
				return HttpResponseRedirect('')
			else:
				context ={'form':form}
				messages.error(request, 'Form submission not successful. Please retry with Valid values')
				return render (request,'bvisa/bvisa_add.html',{'form':form})
		else:
			context ={'form':form}
			messages.error(request, 'Form submission not successful. Please retry with Valid values')
			return render (request,'bvisa/bvisa_add.html',{'form':form})
	else:
		form = BvisaAddForm()
		context = {'form':form}
		return render (request,'bvisa/bvisa_add.html',context)
