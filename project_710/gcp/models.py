from django.db import models
from django.contrib.auth.models import AbstractUser as _AbstractUser, UserManager as _UserManager
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class GCP(models.Model):
	employee_name = models.CharField(max_length=50)
	enterprise_id = models.EmailField(max_length=50)
	PROJECT_OPTIONS = (("Cigna","Cigna"),("Anthem Inc","Anthem Inc"),("Kaiser Permanente","Kaiser Permanente"),("Novartis","Novartis"),("Citi Group","Citi Group"),("Banco Mercantil del Norte","Banco Mercantil del Norte"),("Devon Energy Corporation","Devon Energy Corporation"),("Henkel","Henkel"),("Cigna","Cigna"),("Laureate Education Inc","Laureate Education Inc"),("City of New York","City of New York"),("Best Buy","Best Buy"),("GE Digital","GE Digital"),("Motiva Enterprise LLC","Motiva Enterprise LLC"),("Walt Disney Direct-to-Consumer","Walt Disney Direct-to-Consumer"),("Aetna","Aetna"),("Accenture - Internal Organizations","Accenture - Internal Organizations"),("Freeport-Mcmoran Inc","Freeport-Mcmoran Inc"),("Carrier","Carrier"),("Nadro","Nadro"),("Dont Use-Goldcorp Inc","Dont Use-Goldcorp Inc"),("National Bank of Canada","National Bank of Canada"))
	project = models.CharField(max_length=80,choices=PROJECT_OPTIONS)
	#whatsapp_number_country_code = models.CharField(max_length=5)
	#whatsapp_number = models.DecimalField(max_digits=10,decimal_places=0)
	whatsapp_number=PhoneNumberField()
	travel_start_date = models.DateField()
	CAPABILITY_OPTIONS = (("Data and Analytics","Data and Analytics"),("Oracle","Oracle"),("SAP","SAP"),("Testing and PE","Testing and PE"),("Hostcentric platform","Hostcentric platform"),("Devops","Devops"),("Capital Markets processes","Capital Markets processes"),("Avanade","Avanade"),("Java Tech","Java Tech"))
	capability = models.CharField(max_length=80,choices=CAPABILITY_OPTIONS)

	def __str__(self):
		return self.employee_name