from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gcp_view(request, *args, **kwargs):
	return render (request, "gcp.html",{})


