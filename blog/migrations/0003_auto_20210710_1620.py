# Generated by Django 3.2.5 on 2021-07-10 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210710_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_by',
            new_name='updated_at',
        ),
    ]
