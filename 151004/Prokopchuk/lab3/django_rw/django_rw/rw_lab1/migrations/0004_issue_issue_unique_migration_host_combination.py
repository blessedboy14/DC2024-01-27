# Generated by Django 4.2.11 on 2024-03-20 07:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rw_lab1', '0003_alter_creator_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField(max_length=2048)),
                ('created', models.DateTimeField(default=datetime.datetime(2024, 3, 20, 10, 57, 35, 483020))),
                ('modified', models.DateTimeField(default=datetime.datetime(2024, 3, 20, 10, 57, 35, 483020))),
                ('creatorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rw_lab1.creator')),
            ],
        ),
        migrations.AddConstraint(
            model_name='issue',
            constraint=models.UniqueConstraint(fields=('id', 'title'), name='unique_migration_host_combination'),
        ),
    ]