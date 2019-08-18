"""project_710 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import home_view
from usefulinfo.views import usefulinfo_view
from bvisa.views import bvisa_add_view, bvisa_detail_view
from gcp.views import gcp_view


urlpatterns = [
    path('',home_view,name='home'),
    path('home/',home_view,name='home'),
    path('usefulinfo/',usefulinfo_view,name='usefulinfo'),
    path('bvisa/bvisa_add.html',bvisa_add_view,name='bvisa_add'),
    path('bvisa/detail.html',bvisa_detail_view,name='bvisa_detail'),
    path('gcp/',gcp_view,name='gcp'),
    path('admin/', admin.site.urls),
]
