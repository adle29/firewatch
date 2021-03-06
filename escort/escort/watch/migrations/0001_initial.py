# Generated by Django 2.0 on 2017-12-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firefighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('specialty', models.CharField(max_length=60, null=True)),
                ('sim_ccid', models.CharField(max_length=60, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GasReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('firefighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Firefighter')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('firefighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Firefighter')),
            ],
        ),
        migrations.CreateModel(
            name='TempReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('firefighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Firefighter')),
            ],
        ),
    ]
