# Generated by Django 3.1.1 on 2020-09-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='CAR_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
