import os
import time
import random
import send2trash
import time
from datetime import datetime
from instabot import Bot
from os import listdir
from os.path import isfile, join
from random import randint

i=0
bot = Bot() 
PhotoPath = "/data/data/com.termux/files/home/storage/dcim/Instagram-posts-and-feeds-main/Whatdidido(AwazInstaBot)/bezubaan"  # Change Directory to Folder with Pics that you want to upload
IGUSER = "name" 
PASSWD = "pass"  
#PhotoHashtag
IGCaption = "❤She loved me & i never understood her, she left me, and now i know!  #india #love #instagram #mumbai #photography #indian #delhi #instagood #follow #travel #like #kerala #bhfyp #bollywood #nature #photooftheday #fashion #maharashtra #incredibleindia #likeforlikes #travelphotography #tiktok #art #followforfollowback #rajasthan #insta #picoftheday #ig #pune #bhfyp "
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile (join(PhotoPath, f))])

bot.login(username=IGUSER,password=PASSWD)

while(1):
    now = datetime.now()
    dtcode = now.strftime("%H%M")
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    print("Time =", dtcode)
    bot.upload_photo(photo,caption=IGCaption)
    send2trash.send2trash(photo+str("REMOVE_ME"))
    time.sleep(43200)
    i=i+1
    time.sleep(20)



