# Generated by Django 4.1.4 on 2022-12-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_mainform'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SName', models.CharField(max_length=20)),
                ('LapName', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('Processor', models.CharField(max_length=20)),
                ('Ram', models.CharField(max_length=20)),
                ('Os', models.CharField(max_length=20)),
                ('Amount', models.CharField(max_length=10)),
                ('Mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'db_table': 'demo_laptop',
            },
        ),
        migrations.DeleteModel(
            name='Mainform',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
