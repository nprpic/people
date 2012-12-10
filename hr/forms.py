from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.auth.models import User
from hr.models import Contract


class ContractForm(ModelForm):
	person = ModelMultipleChoiceField(queryset=User.objects.all())

	class Meta:
		model = Contract
		fields = ('type','title','description','weekly_hours','hourly_rate','monthly_salary')