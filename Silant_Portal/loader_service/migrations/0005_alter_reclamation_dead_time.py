# Generated by Django 5.0.6 on 2024-07-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader_service', '0004_alter_reclamation_dead_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamation',
            name='dead_time',
            field=models.IntegerField(null=True),
        ),
    ]
