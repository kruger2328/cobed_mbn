# Generated by Django 3.2.6 on 2021-12-20 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_dmo_status_appruval'),
        ('center', '0023_patient_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.lab'),
        ),
    ]