from django.urls import path
from .views import TextToMp3View

urlpatterns = [
    path('convert_to_mp3/', TextToMp3View.as_view(),name="remove-image-background"),
]
