# Generated by Django 4.2.7 on 2023-11-22 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_osoba_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
