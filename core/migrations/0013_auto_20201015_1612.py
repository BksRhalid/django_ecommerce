# Generated by Django 2.2.14 on 2020-10-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_userprofile_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'NEW'), ('D', 'NON DISPONIBLE'), ('R', 'QUANTITE LIMITEE')], max_length=1),
        ),
    ]
