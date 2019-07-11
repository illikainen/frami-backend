# Generated by Django 2.2.2 on 2019-07-11 15:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import frami.api.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('result', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('unread', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=models.SET(frami.api.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
