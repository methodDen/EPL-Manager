# Generated by Django 3.1.7 on 2021-05-07 09:03

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_footballclub_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='agent_photos', validators=[utils.validators.validate_size, utils.validators.validate_extension]),
        ),
    ]
