# Generated by Django 3.0.3 on 2020-05-14 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200514_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application_model',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='application_model',
            name='property',
        ),
    ]
