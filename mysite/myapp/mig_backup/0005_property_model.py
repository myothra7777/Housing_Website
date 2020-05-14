# Generated by Django 3.0.3 on 2020-04-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200310_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A', 'Apartment'), ('H', 'House')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('num_rooms', models.CharField(max_length=1)),
                ('num_bathrooms', models.CharField(max_length=1)),
                ('sq_footage', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
