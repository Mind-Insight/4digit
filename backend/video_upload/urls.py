from django.urls import path
from . import views

urlpatterns = [
    path(
        "upload/",
        views.video_upload_view,
        name="upload_video",
    ),
    path(
        "results/",
        views.analysis_list_view,
        name="analysis_list",
    ),
    path("", views.analysis_list_view, name="home"),
]
