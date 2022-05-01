import tail  # https://github.com/kasun/python-tail
import telebot #pip install pyTelegramBotAPI
import time
import datetime

filelog='/var/log/YSF' # Cartella dove si trovano i file YSFReflector-.-.-..log

bottoken='xxxxx-xxxxx'  #Token del bot telegram
chat_id='xxxxxxx'                    #ID della chat su cui inviare i messaggi


bot = telebot.TeleBot(bottoken)



def riga(x):
	global tempo, qrz, deltat, gateway
	dati = x.split(' ')
	#print(dati)
	if dati[3] == 'Received' and dati[5] == 'from':
		qrz = dati[6]
		tempo = int(time.time())
		print(tempo)
		gateway = dati[21]
	elif dati[3] == 'Network' and dati[4] == 'watchdog' or dati[3] == 'Received' and dati[4] == 'end':
		deltat = int(time.time()) - tempo
		print(qrz + str(deltat) + gateway)
		bot.send_message(chat_id, 'Call: ' + qrz + '\nGateway: '+ gateway + '\nDurata: ' + str(deltat))
		

tailog = tail.Tail(filelog+'/YSFReflector-'+str(datetime.date.today())+'.log')

tailog.register_callback(riga) #In caso di una nuova riga viene eseguita la funzione "riga" dove x e la nuova riga acquisita

tailog.follow(s=1) # Questo comando imposta la lettura del file log a 1 Secondo (s=1)

