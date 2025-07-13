from django.shortcuts import render, redirect
from .models import FlashCard


def list_flashcards(request):
    context = {}
    flashcards = FlashCard.objects.all()
    context["flashcards"] = flashcards
    return render(
        request,
        "index.html",
        context,
    )


def delete_flashcard(request, id):
    if request.method == "POST":
        try:
            flashcard = FlashCard.objects.get(id=id)
            flashcard.delete()
        except FlashCard.DoesNotExist:
            pass

    return redirect("list_flashcards")
