from django.forms import ModelForm
from billing.models import Customer, Invoice, InvoiceItem, CustomerAlert

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['description', 'first_name', 'last_name', 'email', 'company', 'description', 'phone_number_1', 'phone_number_2', 'website', 'city', 'address_1', 'address_2', 'state', 'zip_code']


class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ['date_due', 'date_paid', 'amount_due', 'work_summary_description', 'customer']

class InvoiceItemForm(ModelForm):
	class Meta:
		model = InvoiceItem
		fields = ['invoice', 'description', 'hours', 'rate', 'total']

class CustomerAlertForm(ModelForm):
	class Meta:
		model = CustomerAlert
		fields = ['customer', 'email_alert', 'email_alert_email', 'text_message_alert', 'text_message_alert_phone']