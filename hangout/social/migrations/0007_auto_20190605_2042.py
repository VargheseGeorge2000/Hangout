# Generated by Django 2.1.5 on 2019-06-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_groups_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='profile_pic',
            field=models.ImageField(default='defaultgroup.png', upload_to=''),
        ),
    ]
