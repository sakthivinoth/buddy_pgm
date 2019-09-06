from django.contrib import admin

# Register your models here.
from .models import Bvisa
from import_export.admin import ImportExportModelAdmin

class BvisaAdmin(ImportExportModelAdmin):
	list_display = [field.attname for field in Bvisa._meta.fields]

admin.site.register(Bvisa,BvisaAdmin)
