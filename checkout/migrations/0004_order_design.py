# Generated by Django 3.0.1 on 2021-04-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210328_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='design',
            field=models.CharField(default='', max_length=254),
        ),
    ]