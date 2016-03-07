from django.forms import ModelForm
from expense.models import Expense

class ExpenseForm(ModelForm):
	
	class Meta:
		model = Expense
		fields = ['description', 'purchase_date', 'total', 'receipt']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})