# Generated by Django 3.2.9 on 2021-12-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_company_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_img',
            field=models.ImageField(default='/home/nicu/Desktop/PoliHackv12/polihack/public/cityImg/pizza.jpg', null=True, upload_to='images/companies'),
        ),
    ]
