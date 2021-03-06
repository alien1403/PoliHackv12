# Generated by Django 3.2.9 on 2021-12-04 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20211204_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.company', verbose_name='name'),
        ),
    ]
