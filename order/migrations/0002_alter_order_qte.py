# Generated by Django 4.2.7 on 2023-12-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='qte',
            field=models.IntegerField(default=1),
        ),
    ]
