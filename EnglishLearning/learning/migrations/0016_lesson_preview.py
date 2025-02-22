# Generated by Django 5.1.5 on 2025-02-19 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0015_tag_lesson_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='preview',
            field=models.TextField(default='This is a preview of the lesson. Please update it.', validators=[django.core.validators.MinLengthValidator(200)]),
            preserve_default=False,
        ),
    ]
