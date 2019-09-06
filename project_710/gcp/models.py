from django.db import models
from django.contrib.auth.models import AbstractUser as _AbstractUser, UserManager as _UserManager
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone


# Create your models here.
class GCP(models.Model):
	employee_name = models.CharField(max_length=20)
	enterprise_id = models.EmailField(max_length=40)
	PROJECT_OPTIONS = (("Cigna","Cigna"),("Anthem","Anthem"))
	project = models.CharField(max_length=20,choices=PROJECT_OPTIONS)
	whatsapp_number_country_code = models.CharField(max_length=5)
	whatsapp_number = models.DecimalField(max_digits=10,decimal_places=0)
	travel_start_date = models.DateField(auto_now=False,auto_now_add=False)
	CAPABILITY_OPTIONS = (("Capability1","Capability1"),("Capability2","Capability2"))
	capability = models.CharField(max_length=20,choices=CAPABILITY_OPTIONS)

	def __str__(self):
		return self.employee_name