# Generated by Django 3.2.9 on 2021-12-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20211204_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
