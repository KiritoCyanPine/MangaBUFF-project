from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import MangaTitles
from django.contrib import messages


# Create your views here.
def mangatitle(request,manga_id):
    manganame = get_object_or_404(MangaTitles, pk = manga_id)
    chapters = manganame.manga_folder()
    print(chapters)
    context = {
    'chapters': chapters,
    'manga':manganame,
    }
    return render(request, "mangaPage.html", context)

def MainPage(request):
    allManga = MangaTitles.objects.all()
    context = {
    'allManga': allManga,
    }
    print(allManga)
    return render(request, "mainPage.html", context)

def mangaChapter(request,manga_id,chapter_id):
    manganame = get_object_or_404(MangaTitles, pk = manga_id)
    allChapters = manganame.manga_folder()
    chapter = allChapters[chapter_id]
    context = {
    'chapter_Images':chapter
    }
    return render(request , "mangachapterPage.html", context)
