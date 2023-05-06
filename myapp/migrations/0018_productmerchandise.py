# Generated by Django 4.2 on 2023-04-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_productbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMerchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=100)),
                ('ddescription', models.TextField()),
                ('pprice', models.CharField(max_length=20)),
                ('ppicture', models.ImageField(upload_to='media/productMerchandise')),
            ],
            options={
                'verbose_name': 'ProductMerchandise',
                'verbose_name_plural': 'ProductMerchandise',
            },
        ),
    ]
