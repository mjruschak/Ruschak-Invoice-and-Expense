from django.db import models

# ---- Expense Model ----
class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    purchase_date = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    receipt = models.URLField(max_length=250)
