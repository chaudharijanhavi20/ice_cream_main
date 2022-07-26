# Generated by Django 3.0.14 on 2022-06-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220611_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=20, max_length=20)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('no_login', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
