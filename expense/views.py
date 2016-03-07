from django.http import Http404
from django.shortcuts import render
from expense.modelforms import ExpenseForm

def expenses(request):
	return render(request, 'list.html')

def expenses_add(request):
	expense_form = ExpenseForm()
	options = {
		'form': expense_form,
		'action': '/expenses/add',
	}
	
	return render(request, 'form.html', options)