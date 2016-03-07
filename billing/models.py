from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField

# ---- Customer Model ----
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number_1 = models.CharField(validators=[phone_regex], blank=True, max_length=25)
    phone_number_2 = models.CharField(validators=[phone_regex], blank=True, max_length=25)
    website = models.URLField(max_length=250, blank=True)
    city = models.CharField(max_length=75)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    state = USStateField(max_length=2, default="NY")
    zip_code = models.CharField(max_length=5)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

# ---- Invoice Model ----
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date_due = models.DateField()
    date_paid = models.DateField(blank=True)
    amount_due = models.DecimalField(max_digits=5, decimal_places=2)
    work_summary_description = models.TextField(blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

# ---- Invoice Items Model ----
class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    description = models.TextField()
    hours = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

# ---- Customer Alert Model ----
class CustomerAlert(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    email_alert = models.BooleanField()
    email_alert_email = models.CharField(max_length=200, blank=True)
    text_message_alert = models.BooleanField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    text_message_alert_phone = models.CharField(validators=[phone_regex], blank=True, max_length=25)
