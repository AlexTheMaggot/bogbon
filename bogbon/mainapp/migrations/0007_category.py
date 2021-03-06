# Generated by Django 3.1.4 on 2021-11-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210826_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=200, verbose_name='Название категории на русском')),
                ('name_uz', models.CharField(max_length=200, verbose_name='Название категории на узбекском')),
                ('name_en', models.CharField(max_length=200, verbose_name='Название категории на английском')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
