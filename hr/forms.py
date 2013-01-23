from django.forms import ModelForm, ModelChoiceField
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from hr.models import Contract, Absence


class ContractForm(ModelForm):
	person = ModelChoiceField(queryset=User.objects.filter(is_active=True))

	class Meta:
		model = Contract
		fields = ('type','title','description','weekly_hours','hourly_rate','monthly_salary')

class AbsenceForm(ModelForm):
	person = ModelChoiceField(queryset=User.objects.filter(is_active=True))
	start = DateField(widget=SelectDateWidget)
	end = DateField(widget=SelectDateWidget)

	class Meta:
		model = Absence