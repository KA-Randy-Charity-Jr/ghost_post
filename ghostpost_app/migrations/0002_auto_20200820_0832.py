# Generated by Django 3.1 on 2020-08-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ghostpost',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
