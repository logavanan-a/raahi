# Generated by Django 4.2.1 on 2023-08-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0055_alter_qrcodegeneration_options_patient_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodegeneration',
            name='range_from',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qrcodegeneration',
            name='range_to',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
