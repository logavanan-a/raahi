# Generated by Django 4.2.1 on 2023-08-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0047_remove_screening_employed_in_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='delay_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
