# Generated by Django 5.1.4 on 2025-01-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
