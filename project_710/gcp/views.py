from django.http import HttpResponse
from django.shortcuts import render

from .forms import GCPAddForm,RawGCPForm
from .models import GCP


def gcp_add_view(request, *args, **kwargs):
	form = RawGCPForm(request.GET)
	context = {"form":form}
	if request.method=="POST":
		form = RawGCPForm(request.POST)
		context ={"form":form}
		if form.is_valid():
			print(form.cleaned_data)
			GCP.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	return render (request,'gcp/gcp_add.html',context)

# def bvisa_add_view(request, *args, **kwargs):
# 	context ={}
# 	if request.method=="POST":
# 		emp_name =request.POST.get("employee_name")
# 		print(emp_name)
# 		#Bvisa.objects.create(employee_name=emp_name)
# 	return render (request,'bvisa/bvisa_add.html',context)

# def bvisa_add_view(request, *args, **kwargs):
# 	form = BvisaAddForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 	context ={'form':form}
#	return render (request,'bvisa/bvisa_add.html',context)

# Create your views here.
def gcp_view(request,*args, **kwargs):
	
	context = {}
	return render (request, "gcp.html",context)


def gcp_detail_view(request, *args, **kwargs):
	obj = GCP.objects.get(id=1)
	context ={'object':obj}
	return render (request,'gcp/gcp_detail.html',context)