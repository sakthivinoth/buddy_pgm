from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def usefulinfo_view(request,*args, **kwargs):
	context = {"hello":'world',"list":[1,2,3,4,5]}
	return render (request, "usefulinfo.html",context)


