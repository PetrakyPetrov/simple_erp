# Generated by Django 2.2.dev20180816134906 on 2018-08-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180825_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_company',
            field=models.BooleanField(default=True),
        ),
    ]