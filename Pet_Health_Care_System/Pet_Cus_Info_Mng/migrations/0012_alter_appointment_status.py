# Generated by Django 4.2.18 on 2025-01-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet_Cus_Info_Mng', '0011_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Chưa thanh toán', 'Chưa thanh toán'), ('Đã thanh toán', 'Đã thanh toán')], max_length=50),
        ),
    ]
