# Generated by Django 2.2.14 on 2020-10-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_payment_points_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='points_used',
            field=models.IntegerField(default=0),
        ),
    ]