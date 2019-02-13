# Generated by Django 2.1.3 on 2018-11-13 18:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0023_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='amazonid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credibilityscore',
            field=models.FloatField(default=1),
        ),
    ]