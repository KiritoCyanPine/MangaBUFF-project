from django.db import models
import os
import re


link_Gen_prefix = 'http://localhost:11112/'


# Create your models here.
class MangaTitles(models.Model):
    title = models.CharField(max_length = 200)
    profile = models.ImageField(upload_to= 'images/profile/')
    genres = models.CharField(max_length=250)
    current_chapter = models.CharField(max_length = 200,blank = True)
    summary = models.TextField()
    directory_address = models.CharField(max_length=250)
    fav = models.BooleanField(blank = True)
    count = models.IntegerField(blank = True)

    def __str__(self):

        return self.title

    def manga_folder(self):
        try:
            img_list  = os.listdir(self.directory_address)
            last_Dir = self.directory_address.split("\\")
            last_Dir = last_Dir[-1]
            print("count ", self.count)
            img_list.sort(key=natural_keys)
            #print(img_list)
            if self.count == 0 or self.count == None:
                firstCh = img_list[0]
                self.current_chapter = firstCh.split('_')[0]
                self.count += 1
            print("count After", self.count)
            mangaChapters = dict()
            ch_def = "someting"
            tempList = list()
            for eachname in img_list:
                ch = eachname.split("_")
                if ch_def == ch[0]:
                    tempList.append(link_Gen_prefix+last_Dir+'/'+eachname)
                else:
                    mangaChapters[ch_def] = tempList[:]
                    ch_def = ch[0]
                    tempList.clear()
                    tempList.append(link_Gen_prefix+last_Dir+'/'+eachname)
            del mangaChapters['someting']
            #for i in mangaChapters:
            #   print(i," :: ",mangaChapters[i])
            #print(mangaChapters)
        except:
            mangaChapters = -1
        return mangaChapters

    def images_in_Folder(self):

        return

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]
