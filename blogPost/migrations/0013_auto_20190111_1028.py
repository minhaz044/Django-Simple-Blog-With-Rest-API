# Generated by Django 2.0.7 on 2019-01-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0012_auto_20190111_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='.'),
        ),
    ]