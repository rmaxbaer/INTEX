# Generated by Django 3.1.4 on 2020-12-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_auto_20201208_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cover_picture',
            field=models.ImageField(blank=True, upload_to='cover_picture/'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_picture/'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, upload_to='resume_files/'),
        ),
    ]
