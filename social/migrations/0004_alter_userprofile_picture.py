# Generated by Django 4.0.3 on 2022-03-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pic.png', upload_to='uploads/profile_pictures'),
        ),
    ]
