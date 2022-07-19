# Generated by Django 3.1.14 on 2022-07-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacturer',
        ),
        migrations.AlterField(
            model_name='car',
            name='body',
            field=models.CharField(choices=[('Est', 'Estate'), ('Sal', 'Saloon'), ('Hatch', 'HatchBack'), ('Van', 'Van')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(help_text=' year of production', verbose_name='made in year'),
        ),
    ]