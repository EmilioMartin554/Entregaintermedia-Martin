# Generated by Django 4.0.6 on 2022-09-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_publicacion', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_publicacion', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_publicacion', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=2000)),
            ],
        ),
    ]
