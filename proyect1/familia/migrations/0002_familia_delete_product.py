# Generated by Django 4.0.6 on 2022-07-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.FloatField()),
                ('habita_en_casa', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]