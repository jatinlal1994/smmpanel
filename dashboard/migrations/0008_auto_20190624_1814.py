# Generated by Django 2.2.1 on 2019-06-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190623_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upi',
            name='number',
        ),
        migrations.AddField(
            model_name='upi',
            name='upi_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
