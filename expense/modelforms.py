from django.forms import ModelForm
from expense.models import Expense

class ExpenseForm(ModelForm):
	class Meta:
		model = Expense
		fields = ['description', 'purchase_date', 'total', 'receipt']