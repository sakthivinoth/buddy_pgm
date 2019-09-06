from django.contrib import admin

# Register your models here.
from .models import GCP
from import_export.admin import ImportExportModelAdmin

class GCPAdmin(ImportExportModelAdmin):
	list_display = [field.attname for field in GCP._meta.fields]

admin.site.register(GCP, GCPAdmin)