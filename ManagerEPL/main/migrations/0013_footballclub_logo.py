# Generated by Django 3.1.7 on 2021-05-07 08:53

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210427_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballclub',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='football_club_photos', validators=[utils.validators.validate_size, utils.validators.validate_extension]),
        ),
    ]