# Generated by Django 4.2.3 on 2023-09-06 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0058_familymember_partner_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spectacletype',
            old_name='follow_up_status',
            new_name='spectacle_status',
        ),
    ]
