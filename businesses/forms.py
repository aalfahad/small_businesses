from django import forms 
from .models import Business

class BusinessForm(forms.ModelForm):
	class meta:
		model = Business
		fields = ['name', 'description','established']