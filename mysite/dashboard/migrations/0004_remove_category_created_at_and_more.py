# Generated by Django 4.2.11 on 2024-04-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='updated_at',
        ),
    ]