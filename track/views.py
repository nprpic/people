from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from track.models import Activity, TimeEntry
#from track.forms import 
from core.models.person import Person


@login_required
def track(request):
	user = User.objects.get(pk=request.user.id)
	all_entries = TimeEntry.objects.filter(person=user.get_profile())
	return render(request, 'entries.html', {'entries':all_entries})


# @login_required
# def add_new_entry(request):
# 	activity_form = ActivityForm(request.POST or None)
# 	entry_form = TimeEntryForm(request.POST or None)
# 	if activity_form.is_valid() and entry_form.is_valid():
# 		activity = activity_form.save(commit=False)
# 		project.client = project_form.cleaned_data['client']
# 		project.save()
# 		return redirect(projects)
# 	messages.warning(request, u', '.join(project_form.errors))
# 	return render(request, 'add_new_project.html', {'form':project_form})