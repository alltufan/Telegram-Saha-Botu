from html.parser import HTMLParser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import datetime
import requests
import json


TOKEN ="TELEGRAM_TOKEN_KEY"
    
def start(update,context):
       update.message.reply_text("<b>Merhaba, Hoşgeldiniz.\nWeb Sitesi: /site \nYoutube: /youtube \nRapor: /rapor \nArıza: /ariza \nMasraf: /masraf \nHava Durumu: /weather</b>",parse_mode = telegram.ParseMode.HTML)

def site(update,context):
       update.message.reply_text("<b>DEEP OFFSHORE Web Sitesi : https://deepoffshore.com</b>",parse_mode = telegram.ParseMode.HTML)

def weather(update,context):
       update.message.reply_text("<b>Hava durumu için :https://www.windy.com</b>",parse_mode = telegram.ParseMode.HTML)

def expenses(update,context):
       data2=update.message.text.split(" ")
       now2=datetime.datetime.now()
       tsp2=now2.timestamp()
       data2_json={"Tarih: ": data2[1],
                   "Aciklama: ": data2[2],
                   "Tutar: ": data2[3],}
       with open("masraf.js","a+") as file:
              json.dump(data2_json,file)
       update.message.reply_text("Masraf Girildi")
       
def breakdown(update,context):
       data= update.message.text
       now = datetime.datetime.now()
       tsp=now.timestamp()
       data_json={"arıza": data,
                  "tarih": tsp,}
       with open("ariza.js","a+") as file:
              json.dump(data_json,file)
       update.message.reply_text("Arıza Kaydı Oluşturuldu")

#def video(update,context):
#      update.message.reply_text("<b>Ali TUFAN Youtube : https://www.youtube.com/channel/UCzG8OnL6CxXXlgETWT1pu6w </b>",parse_mode = telegram.ParseMode.HTML,disable_web_page_preview=True) #disable_web_page_preview=True video ön izlemesini kapatır


def report(update,context):
       data1=update.message.text
       now1=datetime.datetime.now()
       tsp1=now1.timestamp()
       data1_json={"Açıklama: ": data1,
                   "tarih: ": tsp1,}
       with open("rapor.js","a+") as file:
              json.dump(data1_json,file)
       update.message.reply_text("Kayıt Alındı")
    
#def scorring(update,context):
#       update.message.reply_text()

updater=Updater(TOKEN)
#update = telegram.ext.Updater(TOKEN,use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("site",site))
#disp.add_handler(telegram.ext.CommandHandler("youtube",video))
disp.add_handler(telegram.ext.CommandHandler("weather",weather))
disp.add_handler(telegram.ext.CommandHandler("ariza",breakdown))
disp.add_handler(telegram.ext.CommandHandler("rapor",report))
#disp.add_handler(telegram.ext.CommandHandler("puantaj",scorring))
disp.add_handler(telegram.ext.CommandHandler("masraf",expenses))


updater.dispatcher.add_handler(MessageHandler(Filters.text,telegram.Message))
updater.start_polling()
updater.idle()

