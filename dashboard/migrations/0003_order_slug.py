# Generated by Django 2.2.1 on 2019-05-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190527_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.CharField(default='', max_length=256),
        ),
    ]