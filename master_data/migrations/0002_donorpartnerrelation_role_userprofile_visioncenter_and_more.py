# Generated by Django 4.2.1 on 2023-06-05 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorPartnerRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('deactivated_date', models.DateField(blank=True, null=True)),
                ('reason_for_deactivated', models.CharField(blank=True, max_length=150, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Donor Partner Relation',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('role_type', models.IntegerField(choices=[(0, 'Web'), (1, 'App'), (2, 'Both')])),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='VisionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('contact_no', models.CharField(max_length=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.district')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vision Center',
            },
        ),
        migrations.RemoveField(
            model_name='vision_center',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='vision_center',
            name='district',
        ),
        migrations.RemoveField(
            model_name='vision_center',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='vision_center',
            name='partner_name',
        ),
        migrations.RemoveField(
            model_name='vision_center',
            name='state',
        ),
        migrations.AlterModelOptions(
            name='telecalling',
            options={'verbose_name_plural': 'Tele Calling'},
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='name_of_donor',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='masterlookup',
            old_name='partner',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='partner',
            old_name='partner_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='partner_hospitals',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='access_in_web_end_and_tablet',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='role',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='state',
        ),
        migrations.AlterField(
            model_name='donor',
            name='email_id',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='partner',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='partner',
            name='email_id',
            field=models.EmailField(max_length=150),
        ),
        migrations.DeleteModel(
            name='User_profile',
        ),
        migrations.DeleteModel(
            name='Vision_center',
        ),
        migrations.AddField(
            model_name='visioncenter',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.partner'),
        ),
        migrations.AddField(
            model_name='donorpartnerrelation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.donor'),
        ),
        migrations.AddField(
            model_name='donorpartnerrelation',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donorpartnerrelation',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.partner'),
        ),
    ]
