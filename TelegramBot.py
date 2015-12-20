import time
import telebot
import shutil
import os

token='158181658:AAHLsQ6HOVS4k30TtXrdTbfLAK0jF8ED5qw'
bot=telebot.TeleBot(token)

shutil.copy2('/var/log/auth.log','./log')
f=open('./log')
for k in f.readlines():
    line=k
st=line
f.close()

@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    global chat
    chat=message.chat.id
    bot.stop_polling()

if __name__=='__main__':
    bot.polling()
    stroka=''
    while(1):
        shutil.copy2('/var/log/auth.log','./log')
        fb=open('./log')
        flag_vivoda=0
        for k in fb.readlines():
            if flag_vivoda==1:
                stroka+=k
                st=k
            if k==st:
                flag_vivoda=1

        fb.close()
        os.remove('./log')
        fs=open('./log','w')
        print (stroka)
        if stroka != '' and chat!=0:
            bot.send_message(chat,stroka)
            stroka=''
        fs.write(stroka)
        fs.close()
        time.sleep(5)


