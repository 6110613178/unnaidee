# Generated by Django 3.1.2 on 2020-11-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_userun_favarite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userun',
            name='favarite',
        ),
        migrations.AddField(
            model_name='userun',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='userfavorite', to='notebook.NoteBook'),
        ),
    ]
