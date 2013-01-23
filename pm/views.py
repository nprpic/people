from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pm.models import Client, Project
from pm.forms import ClientForm, ProjectForm
from core.models.person import Person


@login_required
def clients(request):
	all_clients = Client.objects.all()
	return render(request, 'clients.html', {'clients':all_clients})


@login_required
def add_new_client(request):
	client_form = ClientForm(request.POST or None)
	if client_form.is_valid():
		client = client_form.save()
		return redirect(clients) 
	messages.warning(request, u', '.join(client_form.errors))
	return render(request, 'add_new_client.html', {'form':client_form})


@login_required
def projects(request):
	all_projects = Project.objects.all()
	return render(request, 'projects.html', {'projects':all_projects})


@login_required
def add_new_project(request):
	project_form = ProjectForm(request.POST or None)
	if project_form.is_valid():
		project = project_form.save(commit=False)
		project.client = project_form.cleaned_data['client']
		project.save()
		return redirect(projects)
	messages.warning(request, u', '.join(project_form.errors))
	return render(request, 'add_new_project.html', {'form':project_form})