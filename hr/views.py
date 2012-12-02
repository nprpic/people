from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def contracts(request):
	return render(request, 'contracts.html')


@login_required
def absences(request):
	return render(request, 'absences.html')