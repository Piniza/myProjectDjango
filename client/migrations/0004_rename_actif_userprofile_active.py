# Generated by Django 4.2.7 on 2023-12-16 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_adress_userprofile_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='actif',
            new_name='active',
        ),
    ]
