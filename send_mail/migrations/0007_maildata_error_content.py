# Generated by Django 4.2.1 on 2023-12-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0006_maildata_syn_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='maildata',
            name='error_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
