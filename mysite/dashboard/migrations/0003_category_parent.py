# Generated by Django 4.2.11 on 2024-04-02 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_category_product_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
            preserve_default=False,
        ),
    ]
