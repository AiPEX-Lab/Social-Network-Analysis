# Generated by Django 2.1.7 on 2019-03-22 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_visitor_login_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='login_count',
        ),
    ]