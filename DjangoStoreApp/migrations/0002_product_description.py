# Generated by Django 3.1.5 on 2021-02-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoStoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
