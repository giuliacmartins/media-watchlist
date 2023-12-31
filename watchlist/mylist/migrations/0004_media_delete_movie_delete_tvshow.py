# Generated by Django 4.1.7 on 2023-06-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0003_movie_tvshow_delete_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster', models.URLField()),
                ('year', models.IntegerField()),
                ('media_type', models.CharField(choices=[('movie', 'Movie'), ('series', 'Series')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='TVShow',
        ),
    ]
