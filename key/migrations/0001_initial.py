# Generated by Django 4.2 on 2023-07-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('class_key', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('key_update', models.CharField(max_length=100)),
            ],
        ),
    ]
