# Generated by Django 3.0.14 on 2022-06-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='gender',
            field=models.CharField(default=20, max_length=50),
        ),
    ]
