# Generated by Django 3.2 on 2021-04-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210423_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Artist Age'),
        ),
    ]
