# Generated by Django 3.1.4 on 2021-08-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_article_img_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img_background',
            field=models.ImageField(default=123, upload_to='article_img/', verbose_name='Фоновое изображение (1920х1080)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='img_post',
            field=models.ImageField(default=123, upload_to='article_img/', verbose_name='Изображение в статье (780х500)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_1',
            field=models.TextField(default=123, verbose_name='Первый абзац на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_1_en',
            field=models.TextField(default=123, verbose_name='Первый абзац на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_1_uz',
            field=models.TextField(default=123, verbose_name='Первый абзац на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_2',
            field=models.TextField(default=123, verbose_name='Второй абзац на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_2_en',
            field=models.TextField(default=123, verbose_name='Второй абзац на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_2_uz',
            field=models.TextField(default=123, verbose_name='Второй абзац на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_3',
            field=models.TextField(default=123, verbose_name='Третий абзац на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_3_en',
            field=models.TextField(default=123, verbose_name='Третий абзац на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_3_uz',
            field=models.TextField(default=123, verbose_name='Третий абзац на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_4',
            field=models.TextField(default=123, verbose_name='Четвертый абзац на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_4_en',
            field=models.TextField(default=123, verbose_name='Четвертый абзац на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_4_uz',
            field=models.TextField(default=123, verbose_name='Четвертый абзац на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_5',
            field=models.TextField(default=123, verbose_name='Пятый абзац на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_5_en',
            field=models.TextField(default=123, verbose_name='Пятый абзац на английском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='par_5_uz',
            field=models.TextField(default=123, verbose_name='Пятый абзац на узбекском'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='img_preview',
            field=models.ImageField(upload_to='article_img/', verbose_name='Миниатюра (334х234)'),
        ),
    ]