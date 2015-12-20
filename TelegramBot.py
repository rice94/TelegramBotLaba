import time
import telebot
import shutil
import os

token='158181658:AAHLsQ6HOVS4k30TtXrdTbfLAK0jF8ED5qw'
bot=telebot.TeleBot(token)

shutil.copy2('/var/log/auth.log','/home/kris/log')
f=open('/home/kris/log')
for k in f.readlines():
    linee=k
st=linee
f.close()
id=0

@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id,message.text)
    print (message.chat.id)
    global id=message.chat.id
    bot.stop_polling()
    

if __name__=='__main__':
    bot.polling()
    while(1):
        shutil.copy2('/var/log/auth.log','/home/kris/log')
        fb=open('/home/kris/log')
        flag_vivoda=0
        stroka=''
        for k in fb.readlines():
            if flag_vivoda==1:
                stroka+=k
                st=k
            if k==st:
                flag_vivoda=1

        stroka='test_log_string'
        fb.close()
        os.remove('/home/kris/log')
        fs=open('/home/kris/log','w')
        print (stroka)
        if stroka != '':
            bot.send_message(id,stroka)
        fs.write(stroka)
        fs.close()
        bot.polling()




