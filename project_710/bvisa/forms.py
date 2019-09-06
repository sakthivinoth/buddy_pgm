from django import forms 
from .models import Bvisa
from datetime import datetime
from django.core.exceptions import ValidationError

class BvisaAddForm(forms.ModelForm):

	class Meta:
		model = Bvisa
		fields = [
		'employee_name',
		'enterprise_id',
		'project',
		'whatsapp_number_country_code',
		'whatsapp_number',
		'travel_start_date',
		'travel_end_date',
		'capability']

	#attrs = {'class':'form-control'}
	
	#widgets = {
	# employee_name =forms.CharField(label='', widget=forms.TextInput()),
	# enterprise_id=forms.CharField(label='', widget=forms.TextInput()),
	# project=forms.Select(choices=Bvisa.PROJECT_OPTIONS),
	# whatsapp_number=forms.CharField(label='', widget=forms.TextInput()),
	# travel_start_date=forms.DateInput(),
	# travel_end_date=forms.DateInput(),
	# capability=forms.Select(choices=Bvisa.CAPABILITY_OPTIONS),
	# def clean_whatsapp_number_country_code(self, *args, **kwargs):





	def clean_employee_name(self, *args, **kwargs):
		employee_name = self.cleaned_data['employee_name']
		if not employee_name:
			raise forms.ValidationError('Please enter your Employee name.')
		return employee_name

	def clean_whatsapp_number(self, *args, **kwargs):
		whatsapp_number_country_code = self.cleaned_data['whatsapp_number_country_code']
		if not whatsapp_number_country_code:
			raise forms.ValidationError('Please enter your Whatsapp Number Country Code.')
		whatsapp_number = self.cleaned_data['whatsapp_number']
		if not whatsapp_number:
			raise forms.ValidationError('Please enter your Whatsapp Number.')
		return str(whatsapp_number_country_code)+"-"+str(whatsapp_number)

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
		if project.lower()  in ['cigna','anthem']:
			return project
		else:
			raise forms.ValidationError("Please enter a valid Project")

	def clean_enterprise_id(self, *args, **kwargs):
		enterprise_id = self.cleaned_data['enterprise_id']
		if not enterprise_id:
			raise forms.ValidationError('Please enter your enterprise email address.')
		return enterprise_id
