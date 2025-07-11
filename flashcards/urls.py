from django.urls import path
from .views import list_flashcards

urlpatterns = [
    path("", list_flashcards, name="list_flashcards"),
]
