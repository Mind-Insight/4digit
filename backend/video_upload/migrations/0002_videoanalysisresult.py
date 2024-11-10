# Generated by Django 5.1.3 on 2024-11-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=255, verbose_name='Имя видео')),
                ('personality_traits', models.JSONField(verbose_name='Тип личности (OCEAN)')),
                ('transcription', models.TextField(verbose_name='Распознанный текст')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
        ),
    ]
