# Generated by Django 4.0.3 on 2022-03-08 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_item_created_at_item_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='pic',
        ),
    ]