# Generated by Django 2.2.14 on 2020-07-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Age', models.IntegerField()),
                ('Dep', models.CharField(max_length=30)),
                ('cgpa', models.IntegerField()),
                ('project', models.CharField(max_length=25)),
                ('clubs', models.CharField(max_length=25)),
            ],
        ),
    ]
