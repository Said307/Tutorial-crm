# Generated by Django 3.1.14 on 2022-07-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20220707_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.CharField(help_text=' country of supplier ', max_length=50),
        ),
    ]