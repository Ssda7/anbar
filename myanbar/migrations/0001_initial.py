# Generated by Django 4.2.2 on 2023-08-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=200)),
                ('tedad', models.IntegerField(default=0)),
                ('prov_name', models.CharField(max_length=200)),
                ('shomare_anbar', models.IntegerField(choices=[(1, 'Yek'), (2, 'Do'), (3, 'Se')])),
            ],
        ),
    ]
