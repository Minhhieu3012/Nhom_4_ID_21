# Generated by Django 5.0.10 on 2025-01-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet_Cus_Info_Mng', '0004_alter_customer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Nam'), ('Female', 'Nữ'), ('Other', 'LGBT')], max_length=10),
        ),
    ]
