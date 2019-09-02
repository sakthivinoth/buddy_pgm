from django.contrib import admin

# Register your models here.
from .models import Bvisa


class BvisaAdmin(admin.ModelAdmin):
	list_display = [field.attname for field in Bvisa._meta.fields]

admin.site.register(Bvisa,BvisaAdmin)
