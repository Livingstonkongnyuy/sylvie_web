# Generated by Django 4.2 on 2023-04-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default=False, upload_to='media/blog')),
                ('occupation', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Testimonies',
                'verbose_name_plural': 'Testimonies',
            },
        ),
    ]
