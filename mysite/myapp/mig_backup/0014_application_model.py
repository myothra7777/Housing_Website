# Generated by Django 3.0.5 on 2020-05-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200506_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=10)),
                ('ssn', models.CharField(max_length=11)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]