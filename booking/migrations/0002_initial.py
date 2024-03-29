# Generated by Django 4.2.7 on 2024-02-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=200, unique=True)),
                ('capacity', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_size', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True)),
                ('reference', models.CharField(max_length=8, unique=True)),
                ('table_number', models.ManyToManyField(to='booking.table')),
            ],
        ),
    ]
