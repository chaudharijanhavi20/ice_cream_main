# Generated by Django 4.0.2 on 2022-06-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_desc_contact_email_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=20, max_length=200),
        ),
    ]
