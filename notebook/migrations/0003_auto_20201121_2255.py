# Generated by Django 3.1.1 on 2020-11-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_compare'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='Ostype',
            field=models.CharField(default='w', max_length=64),
        ),
        migrations.AddField(
            model_name='notebook',
            name='star',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]