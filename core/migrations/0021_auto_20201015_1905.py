# Generated by Django 2.2.14 on 2020-10-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201015_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='wallet',
            field=models.PositiveIntegerField(default=10000, null=True),
        ),
    ]