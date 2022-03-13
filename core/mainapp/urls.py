from django.urls import path

from .api.main_page.resource import MainPage
from .api.topic.resource import Topic


urlpatterns = [
    path('', MainPage.as_view()),
    path('topic/<int:topic_number>', Topic.as_view()),
]
