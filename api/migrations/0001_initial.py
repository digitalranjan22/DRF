# Generated by Django 4.0.6 on 2022-07-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuednt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
