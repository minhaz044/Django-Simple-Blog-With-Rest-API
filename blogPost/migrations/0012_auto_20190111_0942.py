# Generated by Django 2.0.7 on 2019-01-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0011_auto_20190111_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]