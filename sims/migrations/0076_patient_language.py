# Generated by Django 4.2.1 on 2023-12-26 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0048_district_ssmis_id_donor_ssmis_id_partner_ssmis_id_and_more'),
        ('sims', '0075_qrcodegeneration_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.language'),
        ),
    ]
