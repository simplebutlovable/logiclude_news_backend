# Generated by Django 3.2 on 2021-04-21 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_news_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='topoftheweek',
            new_name='top_of_the_week',
        ),
    ]