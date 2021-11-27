
import schedule
import telebot
import feedparser
from threading import Thread
from time import sleep
import json
import urllib.request


TOKEN = "Your token"
bot = telebot.TeleBot(TOKEN)
chat_id = 0000#your chat id

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Ciao, il memino giornaliero dovrebbe arrivare alle 10:30 del mattino")



def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    url = "https://www.reddit.com/r/memes/top.rss?t=day"

    f = feedparser.parse(url)



    url_2 = f.entries[0].link+".json"



    with urllib.request.urlopen(url_2) as url2:
      response = json.loads(url2.read().decode())

    bot.send_message(chat_id,"🤖: Ecco il tuo memino giornaliero, Titolo:")
    bot.send_message(chat_id,"\""+f.entries[0].title+"\"")
    print(response)

    try:
      response[0]['data']['children'][0]['data']['preview']['images'][0]['variants']['mp4']['source']['url']
    except:
      try:
        response[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
      except:
        bot.send_photo(chat_id,f.entries[0].media_thumbnail[0]["url"])
      else:
        bot.send_video(chat_id,response[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url'])
    else:
      bot.send_animation(chat_id,(response[0]['data']['children'][0]['data']['preview']['images'][0]['variants']['mp4']['source']['url'].replace("&amp;", "&")))






if __name__ == "__main__":
    # Create the job in schedule.
    function_to_run()
    '''with this you can schedule the script 
    schedule.every(1).minutes.do(function_to_run)'''

    Thread(target=schedule_checker).start()
    bot.polling()


