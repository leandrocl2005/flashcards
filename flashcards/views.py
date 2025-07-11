from django.shortcuts import render
from .models import FlashCard


def list_flashcards(request):
    context = {}
    flashcards = FlashCard.objects.all()
    context["flashcards"] = flashcards
    return render(request, "index.html", context)
