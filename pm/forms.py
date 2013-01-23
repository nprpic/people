from django.forms import ModelForm, ModelChoiceField
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from pm.models import Client, Project


class ClientForm(ModelForm):

	class Meta:
		model = Client

class ProjectForm(ModelForm):
	client = ModelChoiceField(queryset=Client.objects.filter(is_active=True))
	start = DateField(widget=SelectDateWidget)
	end = DateField(widget=SelectDateWidget)

	class Meta:
		model = Project