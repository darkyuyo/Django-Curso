# Generated by Django 5.1.2 on 2024-11-05 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frasemodel',
            options={'verbose_name': 'Frase', 'verbose_name_plural': 'Frases'},
        ),
        migrations.AlterModelTable(
            name='frasemodel',
            table='Frases',
        ),
    ]
