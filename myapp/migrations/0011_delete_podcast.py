# Generated by Django 4.2 on 2023-04-27 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_podcast_audio_filess_alter_podcast_imagess'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Podcast',
        ),
    ]
