# Generated by Django 4.2.10 on 2024-03-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_case_is_running'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='is_running',
            field=models.BooleanField(default=True),
        ),
    ]
