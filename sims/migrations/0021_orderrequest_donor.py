# Generated by Django 4.2.1 on 2023-07-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0012_userpartnerlinkage'),
        ('sims', '0020_alter_orderrequest_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequest',
            name='donor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.donor'),
        ),
    ]
