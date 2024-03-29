# Generated by Django 2.2.2 on 2019-07-18 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_appointment_appointmentrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='refill_request', to='api.Prescription')),
            ],
        ),
    ]
