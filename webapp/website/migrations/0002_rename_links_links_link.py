# Generated by Django 3.2 on 2022-06-11 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='links',
            new_name='link',
        ),
    ]
