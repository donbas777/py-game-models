# Generated by Django 4.0.2 on 2024-04-03 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_race_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='nickname',
        ),
    ]