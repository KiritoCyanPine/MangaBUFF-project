from django.db import models
import os
import re


# Create your models here.
class MangaTitles(models.Model):
    title = models.CharField(max_length = 200)
    profile = models.ImageField(upload_to= 'images/profile/')
    genres = models.CharField(max_length=250)
    current_chapter = models.CharField(max_length = 200)
    summary = models.TextField()
    directory_address = models.CharField(max_length=250)
    fav = models.BooleanField()

    def __str__(self):
        return self.title

    def manga_folder(self):
        img_list  = os.listdir(self.directory_address)
        img_list.sort(key=natural_keys)
        #print(img_list)
        mangaChapters = dict()
        ch_def = "someting"
        tempList = list()
        for eachname in img_list:
            ch = eachname.split("_")
            if ch_def == ch[0]:
                tempList.append(eachname)
            else:
                mangaChapters[ch_def] = tempList[:]
                ch_def = ch[0]
                tempList.clear()
        del mangaChapters['someting']
        #for i in mangaChapters:
        #   print(i," :: ",mangaChapters[i])
        #print(mangaChapters)
        return mangaChapters

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]
