# Generated by Django 3.2.4 on 2021-06-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]