import time
import telebot
import shutil
import os

token='158181658:AAHLsQ6HOVS4k30TtXrdTbfLAK0jF8ED5qw'
bot=telebot.TeleBot(token)
i = 0
len=-1

shutil.copy2('/var/log/auth.log','/home/groot/Desktop/log')
f=open('/home/groot/Desktop/log')
for k in f.readlines():
    len=len+1
    linee=k
    print (len)
st=linee
f.close()

@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id,st)
    print (message.chat.id)
    #id=message.chat.id


if __name__=='__main__':
    #bot.polling()
    while(1):
        shutil.copy2('/home/groot/Desktop/log','/home/groot/Desktop/log_old')
        shutil.copy2('/var/log/auth.log','/home/groot/Desktop/log')
        fb=open('/home/groot/Desktop/log')
        flag_vivoda=0
        stroka=''
        for k in fb.readlines():
            if flag_vivoda==1:
                #bot.send_message(id,k)
                stroka+=k
                st=k
            if k==st:
                flag_vivoda=1


        fb.close()
        os.remove('/home/groot/Desktop/log')
        fs=open('/home/groot/Desktop/log','w')
        print (stroka)
        if stroka != '':
            bot.send_message(-44485918,stroka)
        fs.write(stroka)
        fs.close()
        time.sleep(10)





