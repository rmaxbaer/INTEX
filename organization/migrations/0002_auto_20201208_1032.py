# Generated by Django 3.1.4 on 2020-12-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='cover_picture',
            field=models.ImageField(blank=True, upload_to='cover_picture/'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_picture/'),
        ),
    ]
