# Generated by Django 5.1.2 on 2024-10-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_stock',
        ),
    ]
