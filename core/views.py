from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
	return render(request, 'add_new_person.html')


@login_required
def save_person(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name','')
		last_name = request.POST.get('last_name','')
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		person = User(first_name=first_name, last_name=last_name, username=username)
		person.set_password(password)
		try:
			person.save()
			return redirect(people)
		except IntegrityError:
			messages.warning(request, 'Username already exists!')
			return redirect(add_new_person)


@login_required
def person_profile(request, user_id):
	person = get_object_or_404(User, pk=user_id)
	return render(request, 'person_profile.html', {'person':person})


@login_required
def delete_person(request, user_id):
	person = User.objects.get(id=user_id).delete()
	return redirect(people)


def autocomplete(request):
	all_persons = User.objects.all()
	val = [{"label":p.first_name + " " + p.last_name, "value":p.id} for p in all_persons]
	return HttpResponse(json.dumps(val), mimetype='application/json')