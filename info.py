import json
import telebot
import random
from telebot import types , util
# from telebot.types import *
from decouple import config
# from googletrans import Translator
import re
import time 
import requests
from bs4 import BeautifulSoup
import threading
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# BOT_TOKEN = config("kiss")
BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

text_messages ={
    "Welcome Privet":"مرحبا بك معك بايثون😎\n",
    "Welcome Group" :"تم ارسال رسالة في الخاص اذا لم تصل الرسالة انقر /start",
    "saying goodbye":u"~ {name} ~ غادر المجموعة 😏",
    "welcomeNewMember":u"اهلا بك ~ {name} ~ في مجموعتنا🙋‍♀️",
    "kicked member":u"تم طرد ~ {name} ~ من الجموعة 😯",
    "Forword message":"ممنوع تحويل الرسائل داخل المجموعة",
    "Forword book":"ممنوع تحويل الكتب ولكن يمكنك تنزيلها في المجموعة",
    "Wrong":"هذا الرابط غير مسموح به هنا",
    "leave":"عذرا لايمكنني البقاء عضو في المجموعة"
    }

