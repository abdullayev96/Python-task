# Generated by Django 4.2.11 on 2024-04-02 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300, verbose_name='Kategoriya:')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Kategoriya_',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=300, verbose_name="Do'kon nomi:")),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.category')),
            ],
            options={
                'verbose_name': "Do'kon_",
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Mahsulot nomi:')),
                ('description', models.TextField(verbose_name='Mahsulot haqida:')),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('activate', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.shop')),
                ('images', models.ManyToManyField(related_name='images', to='dashboard.shop')),
            ],
            options={
                'verbose_name': 'Mahsulot_',
            },
        ),
    ]
