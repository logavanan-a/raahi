# Generated by Django 4.2.1 on 2023-07-07 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master_data', '0018_uservendorlinkage_partnervendorlinkage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisionCenterLinkage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Inactive'), (2, 'Active')], db_index=True, default=2)),
                ('server_created_on', models.DateTimeField(auto_now_add=True)),
                ('server_modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('vision_center', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master_data.visioncenter')),
            ],
            options={
                'verbose_name_plural': 'User VisionCenter Linkage',
            },
        ),
    ]
