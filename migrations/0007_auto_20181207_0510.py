# Generated by Django 2.1.4 on 2018-12-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskphrase', '0006_auto_20181207_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='who',
            name='first_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='who',
            name='last_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
    ]
