# Generated by Django 4.2.15 on 2024-08-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
