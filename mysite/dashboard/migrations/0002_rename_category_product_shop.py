# Generated by Django 4.2.11 on 2024-04-02 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='shop',
        ),
    ]
