# Generated by Django 3.2.19 on 2023-06-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('brand', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('current_price', models.CharField(max_length=10)),
                ('original_price', models.CharField(max_length=10)),
                ('category_path', models.CharField(max_length=25)),
                ('availability', models.ManyToManyField(related_name='product_availability', to='CrawlingAPI.Size')),
                ('colors', models.ManyToManyField(to='CrawlingAPI.Color')),
                ('images_url', models.ManyToManyField(to='CrawlingAPI.Image')),
                ('sizes', models.ManyToManyField(related_name='product_sizes', to='CrawlingAPI.Size')),
            ],
        ),
    ]
