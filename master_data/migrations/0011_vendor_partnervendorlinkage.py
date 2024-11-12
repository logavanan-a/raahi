# Generated by Django 4.2.1 on 2023-06-13 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0010_remove_vendor_created_by_remove_vendor_district_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact_no', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=150)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.district')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='PartnerVendorLinkage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('deactivated_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.partner')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.vendor')),
            ],
            options={
                'verbose_name_plural': 'Partner Vendor Linkage',
            },
        ),
    ]
