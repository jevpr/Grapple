# Generated by Django 5.1.5 on 2025-02-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(choices=[('avatar1.png', 'Avatar 1'), ('avatar2.png', 'Avatar 2'), ('avatar3.png', 'Avatar 3'), ('avatar4.png', 'Avatar 4'), ('avatar5.png', 'Avatar 5')], default='avatar1.png', max_length=50),
        ),
    ]
