from django.contrib import admin

# Register your models here.
from .models import GCP

class GCPAdmin(admin.ModelAdmin):
	list_display = [field.attname for field in GCP._meta.fields]

admin.site.register(GCP, GCPAdmin)