# Generated by Django 4.2.7 on 2023-12-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0007_produit_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='produit',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
