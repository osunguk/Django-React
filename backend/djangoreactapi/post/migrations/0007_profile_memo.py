# Generated by Django 2.2.5 on 2019-09-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20190927_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='memo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
