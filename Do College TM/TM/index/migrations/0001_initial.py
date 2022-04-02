# Generated by Django 3.2.9 on 2022-04-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=15)),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('time_minute', models.CharField(max_length=15)),
            ],
        ),
    ]
