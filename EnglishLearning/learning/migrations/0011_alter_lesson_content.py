# Generated by Django 5.1.5 on 2025-02-14 12:18

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0010_rename_uploaded_by_lesson_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='default'),
        ),
    ]
