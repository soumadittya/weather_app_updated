# Generated by Django 3.0 on 2020-04-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0002_auto_20200401_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selected_cities',
            name='hometown',
            field=models.BooleanField(default=True),
        ),
    ]
