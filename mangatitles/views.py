from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import MangaTitles
from django.contrib import messages
import os


# Create your views here.
def mangatitle(request,manga_id):
    manganame = get_object_or_404(MangaTitles, pk = manga_id)
    chapters = manganame.manga_folder()
    #print(chapters)
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

def favour(request,manga_id):
    manganame = get_object_or_404(MangaTitles, pk = manga_id)
    manganame.fav = not manganame.fav
    manganame.save()
    print("$ manganame.fav",manganame.fav)
    return redirect('mangaPages',manga_id=manga_id)

def mangaChapter(request,manga_id,chapter_id):
    manganame = get_object_or_404(MangaTitles, pk = manga_id)
    manganame.current_chapter = chapter_id
    allChapters = manganame.manga_folder()
    ch_list = list()
    for i in allChapters.keys():
        ch_list.append(i)
    if ch_list.index(chapter_id)-1 is -1:
        previous = -1
    else:
        previous = ch_list[ch_list.index(chapter_id)-1]
    try:
        next = ch_list[ch_list.index(chapter_id)+1]
    except:
        next = -1
    chapter = allChapters[chapter_id]
    manganame.save()
    context = {
    'previous':previous,
    'next':next,
    'manga_id':manga_id,
    'chapter_Images':chapter
    }
    return render(request , "mangachapterPage.html", context)


def notify(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mangas = MangaTitles.objects.all()
    allDirs = [ name for name in os.listdir("D:/Manga") if os.path.isdir(os.path.join("D:/Manga", name)) ]
    registeredDirectoryAddresses = [j.directory_address for j in MangaTitles.objects.all()]
    print("registeredDirectoryAddresses",registeredDirectoryAddresses)
    Registered = []
    for i in allDirs:
        #print("if DIr name  :",Anime_dir+i)
        if "D:\\\Manga\\"+i in registeredDirectoryAddresses:
            Registered.append(i)
    print(" Registered" , Registered)
    Deleted_Manga = []

    Avoid_folder = []
    csv_reader = ""
    try:
        with open(BASE_DIR+"\\Dir_Avoid.qaw", 'r') as csv_file:
            csv_reader = csv_file.read()
            Avoid_folder = csv_reader.split(",")
            if "album.css" in Avoid_folder:
                Avoid_folder = Avoid_folder.remove("album.css")
    except:
        c = open(BASE_DIR+"\\Dir_Avoid.qaw", 'w')
        c.close()
        with open(BASE_DIR+"\\Dir_Avoid.qaw", 'r') as csv_file:
            csv_reader = csv_file.read()
            Avoid_folder = csv_reader.split(",")
            if "album.css" in Avoid_folder:
                Avoid_folder = Avoid_folder.remove("album.css")
    Unregistered = set(allDirs) - set(Registered)
    Unregistered = set(Unregistered) - set(Avoid_folder)
    Unregistered = list(Unregistered)
    Unregistered.sort()
    Unregistered_add = ["D:\\Manga\\"+i for i in Unregistered ]
    Unregistered_links = zip(Unregistered,Unregistered_add)

    for j in MangaTitles.objects.all():
        if j.manga_folder() == "-1":
            Deleted_Manga.append(get_object_or_404(MangaTitles, pk=j.id))
    with open(BASE_DIR+"\\Dir_Avoid.qaw", 'r') as csv_file:
        csv_reader = csv_file.read()
    csv_reader = csv_reader.replace(",","\n")
    print(" Unregistered" , Unregistered)

    print(" Deleted_Manga" , Deleted_Manga)
    context = {

    }
    return render(request , 'notification.html', context)
