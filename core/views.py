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


@login_required
def people(request):
	all_persons = User.objects.filter(is_active=True)
	return render(request, 'people.html', {'persons':all_persons})


@login_required
def add_new_person(request):
	user = User()
	user_form = UserForm(request.POST or None)
	if user_form.is_valid():
		user = user_form.save()
		return redirect(people) 
	return render(request, 'add_new_person.html', {'form':user_form})


@login_required
def welcome(request):
	user_id = request.user.id
	person = get_object_or_404(User, id=user_id)
	return render(request, 'person_profile.html', {'person':person})


@login_required
def person_profile(request, user_id):
	person = get_object_or_404(User, pk=user_id)
	return render(request, 'person_profile.html', {'person':person})


@login_required
def delete_person(request, user_id):
	person = get_object_or_404(User, id=user_id)
	person.is_active = False
	person.save()
	messages.warning(request, 'User deactivated!')
	return redirect(people)


def autocomplete(request):
	all_persons = User.objects.filter(is_active=True)
	val = [{"text":p.first_name + " " + p.last_name, "id":p.id} for p in all_persons]
	return HttpResponse(json.dumps(val), mimetype='application/json')