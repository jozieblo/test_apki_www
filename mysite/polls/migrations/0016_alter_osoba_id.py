# Generated by Django 4.2.7 on 2023-11-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]