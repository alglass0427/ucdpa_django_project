# Generated by Django 5.0.6 on 2024-12-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user_default.png', null=True, upload_to='profiles/'),
        ),
    ]
