# Generated by Django 4.1.7 on 2023-06-06 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0005_mediaitem_delete_media'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MediaItem',
            new_name='Media',
        ),
    ]
