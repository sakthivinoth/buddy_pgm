from django import forms 
from .models import GCP
from datetime import datetime
from django.core.exceptions import ValidationError

class GCPAddForm(forms.ModelForm):
	# employee_name = forms.CharField(required=True,min_length=1, max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Employee Name"}))
	# enterprise_id = forms.CharField(required=True,min_length=1, max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Enterprise Id"}))
	# project = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={"placeholder":"Enter Project Name"}))
	# whatsapp_number = forms.DecimalField()
	# travel_start_date = forms.DateField()
	# travel_end_date = forms.DateField()
	# capability= forms.CharField()

	class Meta:
		model = GCP
		fields = [
		'employee_name',
		'enterprise_id',
		'project',
		'whatsapp_number',
		'travel_start_date',
		'travel_end_date',
		'capability']

		attrs = {'class':'form-control'}
		widgets = {
		'employee_name':forms.TextInput(attrs=attrs),
		'enterprise_id':forms.TextInput(attrs=attrs),
		'project':forms.Select(choices=GCP.PROJECT_OPTIONS,attrs=attrs),

		'whatsapp_number':forms.TextInput(attrs=attrs),

		# 'travel_start_date': forms.SelectDateWidget(empty_label=("Year", "Month", "Day"),
		# attrs=({'class':'btn btn-default dropdown-toggle','required':'true'}),
		# years=[year for year in range(2000,datetime.now().year+1)]
		# ),
		# 'travel_end_date': forms.SelectDateWidget(empty_label=("Year", "Month", "Day"),
		# attrs=({'class':'btn btn-default dropdown-toggle','required':'true'}),
		# years=[year for year in range(2000,datetime.now().year+1)]
		# ),



		'travel_start_date':forms.DateInput(attrs=attrs),
		'travel_end_date':forms.DateInput(attrs=attrs),
		'email':forms.TextInput(attrs=attrs),
		'region':forms.Select(choices=GCP.CAPABILITY_OPTIONS,attrs=attrs),

		}



	def clean_employee_name(self):
		employee_name = self.cleaned_data['employee_name']
		if not employee_name:
			raise ValidationError('Please enter your Employee name.')
		return employee_name

	def clean_whatsapp_number(self):
		whatsapp_number = self.cleaned_data['whatsapp_number']
		if not whatsapp_number or len(whatsapp_number) >10 or len(whatsapp_number) < 10:
			raise ValidationError('Please enter your Whatsapp Number.')
		return whatsapp_number

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

# class RawGCPForm(forms.Form):
# 	employee_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Employee Name"}))
# 	enterprise_id = forms.CharField(required=True)
# 	project = forms.CharField()
# 	whatsapp_number = forms.DecimalField()
# 	travel_start_date = forms.DateField()
# 	travel_end_date = forms.DateField()
# 	capability= forms.CharField() #widgets

