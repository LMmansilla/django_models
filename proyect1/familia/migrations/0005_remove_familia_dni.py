# Generated by Django 4.0.6 on 2022-07-29 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0004_alter_familia_dni_alter_familia_habita_en_casa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='dni',
        ),
    ]
