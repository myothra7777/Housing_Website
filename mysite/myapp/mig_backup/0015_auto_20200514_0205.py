# Generated by Django 3.0.3 on 2020-05-14 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_application_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application_model',
            old_name='address',
            new_name='cur_address',
        ),
    ]
