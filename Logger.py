import time
import telebot
import shutil
import os

token='140529463:AAGqcz0mvu--svjePjI6XEuV5QhHNgkB50o'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['ssh'])
def echo_msg(message):
    chatid=message.chat.id
    len=0
    i=0
    stroka=''
    shutil.copy2('/var/log/auth.log','./log.log')
    f=open('./log.log')
    for k in f.readlines():
        len+=1
    f.close()
    f=open('./log.log')
    for k in f.readlines():
        i+=1
        if i>len-10:
            stroka+=k+'\n'
    f.close()
    sti=open('./2.jpg','rb')
    #res=bot.send_photo(chatid,sti,None)
    #print (res)
    #time.sleep(1)
    bot.send_message(chatid,stroka)
    #time.sleep(1)
    #sti=open('./2.jpg','rb')
    #bot.send_photo(chatid,sti)
    print (message.chat.id)
    id=message.chat.id

if __name__=='__main__':
    bot.polling(none_stop=True)






