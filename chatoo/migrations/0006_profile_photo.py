# Generated by Django 4.0.4 on 2022-05-25 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatoo', '0005_userprofileinfo_delete_uploadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
