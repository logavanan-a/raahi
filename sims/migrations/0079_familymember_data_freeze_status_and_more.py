# Generated by Django 4.2.1 on 2023-12-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0078_patient_data_freeze_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='data_freeze_status',
            field=models.IntegerField(choices=[(1, 'Synced'), (2, 'Not Synced')], default=2),
        ),
        migrations.AddField(
            model_name='glassprescription',
            name='data_freeze_status',
            field=models.IntegerField(choices=[(1, 'Synced'), (2, 'Not Synced')], default=2),
        ),
        migrations.AddField(
            model_name='screening',
            name='data_freeze_status',
            field=models.IntegerField(choices=[(1, 'Synced'), (2, 'Not Synced')], default=2),
        ),
        migrations.AddField(
            model_name='spectacletype',
            name='data_freeze_status',
            field=models.IntegerField(choices=[(1, 'Synced'), (2, 'Not Synced')], default=2),
        ),
        migrations.AddField(
            model_name='visualacuity',
            name='data_freeze_status',
            field=models.IntegerField(choices=[(1, 'Synced'), (2, 'Not Synced')], default=2),
        ),
    ]
