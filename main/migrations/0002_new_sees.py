# Generated by Django 4.2.4 on 2023-08-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='sees',
            field=models.IntegerField(default=65),
        ),
    ]