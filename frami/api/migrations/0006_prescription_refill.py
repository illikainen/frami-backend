# Generated by Django 2.2.2 on 2019-07-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='refill',
            field=models.PositiveIntegerField(default=1),
        ),
    ]