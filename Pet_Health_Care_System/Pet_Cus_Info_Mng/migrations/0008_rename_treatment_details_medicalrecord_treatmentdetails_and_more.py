# Generated by Django 5.0.10 on 2025-01-19 09:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet_Cus_Info_Mng', '0007_rename_date_of_birth_pet_dateofbirth_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalrecord',
            old_name='treatment_details',
            new_name='treatmentDetails',
        ),
        migrations.AlterField(
            model_name='pet',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Đang chờ xử lý'), ('completed', 'Đã hoàn thành'), ('failed', 'Thất bại')], default='pending', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Pet_Cus_Info_Mng.customer')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='Pet_Cus_Info_Mng.pet')),
            ],
        ),
    ]
