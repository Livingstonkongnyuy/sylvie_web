# Generated by Django 4.2 on 2023-04-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_productmerchandise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ebook_file', models.FileField(upload_to='media/ebooks')),
            ],
        ),
    ]
