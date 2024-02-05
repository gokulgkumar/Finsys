# Generated by Django 3.2.22 on 2024-01-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_vendor_opblnc_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill',
            name='amtrecvd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='bill_no',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='purchasepayment1',
            name='amountdue',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchasepayment1',
            name='payments',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
