# Generated by Django 4.2 on 2023-04-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_testimonies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default=False, upload_to='media/blog')),
                ('date_published', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcast',
            },
        ),
    ]
