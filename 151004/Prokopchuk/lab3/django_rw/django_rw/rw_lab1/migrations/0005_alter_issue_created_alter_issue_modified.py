# Generated by Django 4.2.11 on 2024-03-20 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw_lab1', '0004_issue_issue_unique_migration_host_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 11, 1, 38, 510938)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 11, 1, 38, 510938)),
        ),
    ]