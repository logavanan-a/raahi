# Generated by Django 4.2.1 on 2023-08-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0031_donor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
