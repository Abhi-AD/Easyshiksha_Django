# Generated by Django 5.1.2 on 2024-10-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albume',
            name='albume_logo',
            field=models.FileField(upload_to=''),
        ),
    ]