# Generated by Django 3.1.2 on 2020-10-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_color_pattern'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('href', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]