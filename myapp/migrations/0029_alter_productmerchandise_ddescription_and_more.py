# Generated by Django 4.2 on 2023-05-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_productmerchandise_ddescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmerchandise',
            name='ddescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productmerchandise',
            name='pprice',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productmerchandise',
            name='ttitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
