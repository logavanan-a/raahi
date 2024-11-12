# Generated by Django 4.2.1 on 2023-07-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0036_patient_donor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glassprescription',
            old_name='patient_uuid',
            new_name='screening_uuid',
        ),
        migrations.AddField(
            model_name='glassprescription',
            name='follow_up_status',
            field=models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Completed')], default=1, null=True),
        ),
    ]
