# Generated by Django 3.2.22 on 2024-01-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_salarydetails1_leave_deduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='convert_invoice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='convert_reinvoice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='convert_salesorder',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
