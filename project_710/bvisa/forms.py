from django import forms 
from .models import Bvisa


class BvisaAddForm(forms.ModelForm):
	employee_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Employee Name"}))
	enterprise_id = forms.CharField(required=True)
	project = forms.CharField()
	whatsapp_number = forms.DecimalField()
	travel_start_date = forms.DateField()
	travel_end_date = forms.DateField()
	capability= forms.CharField()
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

	def clean_project(self, *args, **Kwargs):
		project = self.cleaned_data.get('project')
		if project.lower()  in ['cigna','anthem']:
			return project
		else:
			raise forms.ValidationError("Please enter a valid Project")

class RawBvisaForm(forms.Form):
	employee_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Employee Name"}))
	enterprise_id = forms.CharField(required=True)
	project = forms.CharField()
	whatsapp_number = forms.DecimalField()
	travel_start_date = forms.DateField()
	travel_end_date = forms.DateField()
	capability= forms.CharField() #widgets
