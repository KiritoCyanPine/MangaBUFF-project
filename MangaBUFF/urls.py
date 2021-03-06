"""MangaBUFF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import mangatitles.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mangatitles.views.MainPage, name="MainPage"),
    path('Favourite/', mangatitles.views.Favourite_manga, name="Favourite_manga"),
    path('mangatitle/<int:manga_id>', mangatitles.views.mangatitle, name="mangaPages"),
    path('mangatitle/fav/<int:manga_id>', mangatitles.views.favour, name="Favourite"),
    path('notify/', mangatitles.views.notify, name="notify"),
    path('mangatitle/<int:manga_id>/<str:chapter_id>',mangatitles.views.mangaChapter,name="chapter"),

    path('MangaBird/',mangatitles.views.open_manga_bird, name="MangaBird"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
