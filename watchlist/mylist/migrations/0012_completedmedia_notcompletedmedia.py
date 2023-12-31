# Generated by Django 4.1.7 on 2023-06-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0011_remove_notcompletedmedia_media_delete_completedmedia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_title', models.CharField(max_length=255)),
                ('comp_poster', models.URLField()),
                ('comp_year', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='NotCompletedMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notcomp_title', models.CharField(max_length=255)),
                ('notcomp_poster', models.URLField()),
                ('notcomp_year', models.CharField(max_length=9)),
            ],
        ),
    ]
