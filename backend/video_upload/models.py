from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="videos/")
    processed = models.BooleanField(default=False)
    prediction = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title


from django.db import models


class VideoAnalysisResult(models.Model):
    video_name = models.CharField(max_length=255, verbose_name="Имя видео")
    personality_traits = models.JSONField(verbose_name="Тип личности (OCEAN)")
    transcription = models.TextField(verbose_name="Распознанный текст")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"{self.video_name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
