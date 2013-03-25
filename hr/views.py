from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from hr.models import Contract, Absence
from hr.forms import ContractForm, AbsenceForm
from core.models.person import Person

import json

@login_required
def contracts(request):
	all_contracts = Contract.objects.filter(person__user__is_active=True)
	return render(request, 'contracts.html', {'contracts':all_contracts})


@login_required
def add_new_contract(request):
	contract_form = ContractForm(request.POST or None)
	if contract_form.is_valid():
		contract = contract_form.save(commit=False)
		contract.person = contract_form.cleaned_data['person'].get_profile()
		contract.save()
		return redirect(contracts) 
	messages.warning(request, u', '.join(contract_form.errors))
	return render(request, 'add_new_contract.html', {'form':contract_form})


@login_required
def delete_contract(request, contract_id):
	contract = get_object_or_404(Contract, id=contract_id)
	contract.delete()
	messages.warning(request, 'Contract deleted!')
	return redirect(contracts)


@login_required
def absences(request):
	all_absences = Absence.objects.all()
	return render(request, 'absences.html', {'absences':all_absences})


@login_required
def add_new_absence(request):
	absence_form = AbsenceForm(request.POST or None)
	if absence_form.is_valid():
		absence = absence_form.save(commit=False)
		absence.person = absence_form.cleaned_data['person'].get_profile()
		absence.save()
		return redirect(absences)
	messages.warning(request, u', '.join(absence_form.errors))
	return render(request, 'add_new_absence.html', {'form':absence_form})

# to do: izbaciti duple osobe iz autocompletea
def autocomplete_contract(request):
	all_contracts = Contract.objects.filter(person__user__is_active=True)\
	  .values('person__id', 'person__user__first_name', 'person__user__last_name')\
	  .annotate(Count("person__id"))
	val = [{
		"text": p['person__user__first_name'] + " " + p['person__user__last_name'],
		"id": p['person__id']
	} for p in all_contracts]
	return HttpResponse(json.dumps(val), mimetype='application/json')



 