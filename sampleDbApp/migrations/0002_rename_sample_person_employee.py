# Generated by Django 5.0 on 2023-12-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleDbApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sample_person',
            new_name='Employee',
        ),
    ]
