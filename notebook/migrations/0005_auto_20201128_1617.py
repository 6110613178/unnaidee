# Generated by Django 3.1.1 on 2020-11-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20201121_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='userun',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='notebookdata',
            name='weight',
            field=models.CharField(max_length=64),
        ),
    ]