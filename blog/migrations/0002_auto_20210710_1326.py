# Generated by Django 3.2.5 on 2021-07-10 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='published_by',
        ),
    ]