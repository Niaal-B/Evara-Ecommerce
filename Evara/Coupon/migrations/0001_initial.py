# Generated by Django 5.1.2 on 2024-11-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_purchase_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('usage_limit', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
