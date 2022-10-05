from django.urls import path

from cnabs.views import GetTable

urlpatterns = [
    path("test/", GetTable.as_view()),
]
