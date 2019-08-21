from django.db import models

# Create your models here.
class Bvisa(models.Model):
	employee_name = models.CharField(max_length=70)
	enterprise_id = models.EmailField(max_length=70)
	project = models.CharField(max_length=70)
	whatsapp_number = models.DecimalField(max_digits=10,decimal_places=0)
	travel_start_date = models.DateField(auto_now=False,auto_now_add=False)
	travel_end_date =  models.DateField(auto_now=False,auto_now_add=False)
	CAPABILITY_OPTIONS = (("1","option1"),("2","option2"))
	capability = models.CharField(max_length=1,choices=CAPABILITY_OPTIONS)