from django import forms 
from .models import Bvisa
from datetime import datetime
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput
from phonenumber_field.modelfields import PhoneNumberField

class DateInput(forms.DateInput):
    input_type = 'date'


class BvisaAddForm(forms.ModelForm):

	class Meta:
		model = Bvisa
		fields = [
		'employee_name',
		'enterprise_id',
		'project',
		'whatsapp_number',
		'travel_start_date',
		'travel_end_date',
		'capability']


		widgets = {
		            'travel_start_date': DateInput(),
		            'travel_end_date': DateInput(),
		        }


	def clean_employee_name(self, *args, **kwargs):
		employee_name = self.cleaned_data['employee_name']
		if not employee_name:
			raise forms.ValidationError('Please enter your Employee name.')
		return employee_name

	def clean_whatsapp_number(self, *args, **kwargs):
		whatsapp_number = self.cleaned_data['whatsapp_number']
		if not whatsapp_number:
			raise ValidationError('Please enter your Whatsapp Number.')
		return whatsapp_number

	def clean_travel_start_date(self, *args, **kwargs):
		travel_start_date = self.cleaned_data['travel_start_date']
		if not travel_start_date:
			raise forms.ValidationError('Please enter your Travel start date.')
		return travel_start_date

	def clean_travel_end_date(self, *args, **kwargs):
		travel_end_date = self.cleaned_data['travel_end_date']
		if not travel_end_date:
			raise forms.ValidationError('Please enter your Travel end date.')
		return travel_end_date

	def clean_project(self, *args, **Kwargs):
		project = self.cleaned_data.get('project')
		if project:
			return project
		else:
			raise forms.ValidationError("Please enter a valid Project")

	def clean_enterprise_id(self, *args, **kwargs):
		enterprise_id = self.cleaned_data['enterprise_id']
		if not enterprise_id or 'accenture' not in enterprise_id.lower():
			raise forms.ValidationError('Please enter your Accenture enterprise email address.')
		return enterprise_id
