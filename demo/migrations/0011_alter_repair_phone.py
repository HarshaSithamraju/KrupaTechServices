# Generated by Django 4.1.4 on 2023-02-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_alter_repair_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='Phone',
            field=models.IntegerField(max_length=10),
        ),
    ]