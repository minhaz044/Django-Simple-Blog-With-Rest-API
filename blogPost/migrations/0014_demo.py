# Generated by Django 2.0.7 on 2019-01-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0013_auto_20190111_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='.')),
            ],
        ),
    ]
