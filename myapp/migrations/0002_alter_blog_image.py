# Generated by Django 4.2 on 2023-04-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(height_field=100, upload_to='media/blog', width_field=100),
        ),
    ]
