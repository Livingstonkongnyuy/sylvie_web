# Generated by Django 4.2 on 2023-05-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_productmerchandise_ddescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonies',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='testimonies',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
