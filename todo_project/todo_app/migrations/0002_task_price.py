# Generated by Django 3.2 on 2021-05-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
