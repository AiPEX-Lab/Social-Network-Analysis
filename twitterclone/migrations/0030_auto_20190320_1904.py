# Generated by Django 2.1.3 on 2019-03-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0029_auto_20190319_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
