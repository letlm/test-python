from django.urls import path

from cnabs.views import ReturnInfos

urlpatterns = [
    path("cnabs/", ReturnInfos.as_view()),
]
