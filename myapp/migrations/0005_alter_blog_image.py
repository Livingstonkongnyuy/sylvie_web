# Generated by Django 4.2 on 2023-04-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_blog_date_created_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=False, upload_to='media/blog'),
        ),
    ]
