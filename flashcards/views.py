from django.shortcuts import render


def list_flashcards(request):
    context = {}
    return render(request, "index.html", context)
