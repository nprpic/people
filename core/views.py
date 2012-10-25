from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core.forms import UserForm

import json


def index(request):
    return render(request, 'login.html')


def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			request.session['username'] = username
			return redirect(people)
		else:
			messages.warning(request, 'Incorrect username or password.')
			return redirect(index)


def logout_view(request):
	logout(request)
	return redirect(index)


@login_required
def people(request):
	all_persons = User.objects.all()
	return render(request, 'people.html', {'persons':all_persons})


@login_required
def add_new_person(request):
	new_user_form = UserForm(request.POST)
	return render(request, 'add_new_person.html', {'form':new_user_form})


@login_required
def save_person(request):
	if request.method == 'POST':
		user = User()
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			u = form.save()
			return redirect(people)
		else:
			messages.warning(request, 'Username already exists!')
			return redirect(add_new_person)


@login_required
def person_profile(request, user_id):
	person = get_object_or_404(User, pk=user_id)
	return render(request, 'person_profile.html', {'person':person})


@login_required
def delete_person(request, user_id):
	person = get_object_or_404(User, id=user_id).delete()
	return redirect(people)


def autocomplete(request):
	all_persons = User.objects.all()
	val = [{"label":p.first_name + " " + p.last_name, "value":p.id} for p in all_persons]
	return HttpResponse(json.dumps(val), mimetype='application/json')