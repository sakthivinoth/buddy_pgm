from django import forms 
from .models import GCP
from datetime import datetime
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

class GCPAddForm(forms.ModelForm):

	class Meta:
		model = GCP
		fields = [
		'employee_name',
		'enterprise_id',
		'project',
		'whatsapp_number_country_code',
		'whatsapp_number',
		'travel_start_date',
		'capability']

		widgets = {
		            'travel_start_date': DateInput(),
		            'travel_end_date': DateInput(),
		        }
		# attrs = {'class':'form-control'}
		# widgets = {
		# 'employee_name':forms.TextInput(attrs=attrs),
		# 'enterprise_id':forms.TextInput(attrs=attrs),
		# 'project':forms.Select(choices=GCP.PROJECT_OPTIONS,attrs=attrs),
		# 'whatsapp_number':forms.TextInput(attrs=attrs),
		# 'travel_start_date':forms.DateInput(attrs=attrs),
		# 'travel_end_date':forms.DateInput(attrs=attrs),
		# 'email':forms.TextInput(attrs=attrs),
		# 'region':forms.Select(choices=GCP.CAPABILITY_OPTIONS,attrs=attrs),

		# }



	def clean_employee_name(self):
		employee_name = self.cleaned_data['employee_name']
		if not employee_name:
			raise ValidationError('Please enter your Employee name.')
		return employee_name

	def clean_whatsapp_number(self, *args, **kwargs):
		whatsapp_number_country_code = self.cleaned_data['whatsapp_number_country_code']
		if not whatsapp_number_country_code:
			raise forms.ValidationError('Please enter your Whatsapp Number Country Code.')
		whatsapp_number = self.cleaned_data['whatsapp_number']
		if not whatsapp_number:
			raise forms.ValidationError('Please enter your Whatsapp Number.')
		return str(whatsapp_number_country_code)+"-"+str(whatsapp_number)
		
	def clean_travel_start_date(self):
		travel_start_date = self.cleaned_data['travel_start_date']
		if not travel_start_date:
			raise ValidationError('Please enter your Travel start date.')
		return travel_start_date

	def clean_travel_end_date(self):
		travel_end_date = self.cleaned_data['travel_end_date']
		if not travel_end_date:
			raise ValidationError('Please enter your Travel end date.')
		return travel_end_date

	def clean_project(self, *args, **Kwargs):
		project = self.cleaned_data.get('project')
		if project.lower()  in ['cigna','anthem']:
			return project
		else:
			raise forms.ValidationError("Please enter a valid Project")

	def clean_enterprise_id(self):
		enterprise_id = self.cleaned_data['enterprise_id']
		if not enterprise_id:
			raise ValidationError('Please enter your enterprise email address.')
		return enterprise_id
