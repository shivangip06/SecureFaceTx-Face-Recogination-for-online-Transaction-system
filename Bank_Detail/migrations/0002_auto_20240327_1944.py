# Generated by Django 3.1.1 on 2024-03-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank_Detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='creditmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
