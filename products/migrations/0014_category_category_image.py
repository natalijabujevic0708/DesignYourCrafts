# Generated by Django 3.0.1 on 2021-05-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20201104_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]