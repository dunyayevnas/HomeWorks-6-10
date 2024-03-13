# Generated by Django 5.0.3 on 2024-03-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Pupil name')),
                ('age', models.IntegerField(verbose_name='Pupil age')),
                ('mark_1', models.IntegerField(verbose_name='First month')),
                ('mark_2', models.IntegerField(verbose_name='Second month')),
                ('mark_3', models.IntegerField(verbose_name='Third month')),
                ('mark_4', models.IntegerField(verbose_name='Fourth month')),
                ('mark_5', models.IntegerField(verbose_name='Fifth month')),
                ('mark_6', models.IntegerField(verbose_name='Sixth month')),
            ],
            options={
                'verbose_name': 'Pupils list',
                'db_table': 'pupils',
            },
        ),
    ]
