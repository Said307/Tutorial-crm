# Generated by Django 3.1.14 on 2022-07-04 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20220704_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(help_text=' year of production', validators=[django.core.validators.MinValueValidator(1904), django.core.validators.MaxValueValidator(2022)], verbose_name='made in year'),
        ),
    ]