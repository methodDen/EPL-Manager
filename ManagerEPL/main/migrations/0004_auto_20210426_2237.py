# Generated by Django 3.1.7 on 2021-04-26 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210426_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footballclub',
            old_name='statistics',
            new_name='team_statistics',
        ),
    ]
