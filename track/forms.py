from django.forms import ModelForm, ModelChoiceField
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from track.models import Activity, TimeEntry
from core.models.person import Person


class ActivityForm(ModelForm):

	class Meta:
		model = Activity

class TimeEntryForm(ModelForm):
	project = ModelChoiceField(queryset=Project.objects.all())
	# ovo mora biti aktivnost koju je upravo unio
	activity = ModelChoiceField(queryset=Activity.objects.all())
	# ovo mora biti trenutno logirani user
	person = ModelChoiceField(queryset=User.objects.filter(is_active=True))
	# ovo moraju biti sati i minute
	start = DateField(widget=SelectDateWidget)
	end = DateField(widget=SelectDateWidget)

	class Meta:
		model = Project
