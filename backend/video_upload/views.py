from django.shortcuts import render
from django.http import JsonResponse
from .forms import VideoUploadForm
from .utils import analyze_video
from django.conf import settings
import os
from .models import VideoAnalysisResult


MODEL_PATH = settings.BASE_DIR / "personality_model.pth"


def video_upload_view(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES["video_file"]
            temp_video_path = f"media/videos/{video_file.name}"

            with open(temp_video_path, "wb+") as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)
            try:
                personality_traits, transcription = analyze_video(
                    temp_video_path, MODEL_PATH
                )
                os.remove(temp_video_path)
                result = VideoAnalysisResult.objects.create(
                    video_name=video_file.name,
                    personality_traits=personality_traits.tolist(),
                    transcription=transcription,
                )
                return render(
                    request,
                    "video_results.html",
                    {
                        "personality_traits": personality_traits,
                        "transcription": transcription,
                    },
                )

            except Exception as e:
                if os.path.exists(temp_video_path):
                    os.remove(temp_video_path)
                return render(
                    request,
                    "upload_video.html",
                    {"form": form, "error": f"Ошибка обработки: {str(e)}"},
                )

    else:
        form = VideoUploadForm()

    return render(request, "upload_video.html", {"form": form})


def analysis_list_view(request):
    results = VideoAnalysisResult.objects.all().order_by("-uploaded_at")
    return render(request, "list.html", {"results": results})
