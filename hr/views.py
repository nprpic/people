from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from hr.models import Contract
from hr.forms import ContractForm


@login_required
def contracts(request):
	return render(request, 'contracts.html')


@login_required
def add_new_contract(request):
	contract = Contract()
	contract_form = ContractForm(request.POST or None)
	if contract_form.is_valid():
		contract = contract_form.save()
		return redirect(conracts) 
	return render(request, 'add_new_contract.html', {'form':contract_form})


@login_required
def absences(request):
	return render(request, 'absences.html')