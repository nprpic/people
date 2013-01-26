from django.forms import ModelForm, ModelChoiceField
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from pm.models import Client, Project, Allocation
from core.models.person import Person


class ClientForm(ModelForm):

	class Meta:
		model = Client

class ProjectForm(ModelForm):
	client = ModelChoiceField(queryset=Client.objects.filter(is_active=True))
	start = DateField(widget=SelectDateWidget)
	end = DateField(widget=SelectDateWidget)

	class Meta:
		model = Project

class AllocationForm(ModelForm):
	project = ModelChoiceField(queryset=Project.objects.all())
	person = ModelChoiceField(queryset=User.objects.filter(is_active=True))
	start = DateField(widget=SelectDateWidget)
	end = DateField(widget=SelectDateWidget)
	weekly_hours = DateField(widget=SelectDateWidget)

	class Meta:
		model = Allocation
		exclude = ('person',)