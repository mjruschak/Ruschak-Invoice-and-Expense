# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 01:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('phone_number_2', models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True, max_length=250)),
                ('city', models.CharField(max_length=75)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=5)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_due', models.DateField()),
                ('date_paid', models.DateField(blank=True)),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=5)),
                ('work_summary_description', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Customer')),
            ],
        ),
    ]
