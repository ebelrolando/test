#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
import telegram.ext
import random

def start(bot, update):
    update.message.reply_text("Hola, ¿En qué puedo ayudarte? 😀")

def ayuda(bot, update):
    update.message.reply_text("""Aprende los mejores trucos SEO con PasionSeo.

Aprende un nuevo consejo con el comando /consejo o un sitio con Dofollow con el comando /dofollow.

¡Y si quieres estar al día con articulos del sector, visita www.pasionseo.com!""")

def consejo(bot, update):
	lista = [
		"Si lo que tienes es un negocio local, puede interesarte la aplicación Foursquare, con ella podrás recompensar a los clientes que acuden frecuentemente a tu establecimiento; El Corte Inglés, Jimmy Choo, Dominios pizza, Telepizza, Danone, Pepsi, Lufthansa,… y muchas otras marcas han hecho sorteos, retos y gynkanas maravillosas con esta aplicación y, a su vez, haciendo ruido en las redes sociales.", 
		"No me pongas un código QR enorme si después de molestarme en echar la foto me vas a llevar a tu HOME. ERROR. 7 de cada 10 personas que han abierto un QR afirman que no mereció la pena.", 
		"Para que la experiencia de compra sea única, debemos centrarnos previamente en entender el comportamiento del cliente o consumidor. Y luego, darle paso a la tecnología.",
		"El Email Marketing es una de las acciones mas rápidas de realizar,  reduciendo el tiempo y el esfuerzo en enviar las novedades de una web, tanto si es información o productos para un e-commerce.",
		"El Email Marketing es fácilmente medible en repercusión y efectividad. Mensajes enviados, recibidos, abiertos, geolocalizados (y un largo etc.)",
		"En cuanto a la publicación de fotos en Instagram y la utilización de tu perfil como escaparate para las marcas, realmente está demostrado que esta clase de marketing de contenidos funciona y muy bien.",
		"La inyeccion de Likes en las publicaciones o reproduccion en el caso de los videos, se utiliza para nivelar la balanza de las continuas restriucciones de algoritmo de Instagram, el mismo que hemos sufrido en Facebook.",
	]
	update.message.reply_text(random.choice(lista))

def dofollow(bot, update):
	chat_id = update.message.chat_id
	lista = [
		("http://os.dotq.org/", "dofollow1.png"),
		("http://www.internetmarketing-tipps.de/", "dofollow2.png"),
		("http://www.repossessedcars2009.com/", "dofollow3.png"),
		("http://prohumorist.com/", "dofollow4.png"),
	]
	choice = random.choice(lista)
	bot.send_photo(chat_id=chat_id, photo=open("imagenes/{}".format(choice[1]), 'rb'))
	update.message.reply_text(choice[0])

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = telegram.ext.Updater("512361253:AABCjU33hDwcsWV8n6Z9kYbBqLGhi3e-APc")
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler("start", start))
    dp.add_handler(telegram.ext.CommandHandler("ayuda", ayuda))
    dp.add_handler(telegram.ext.CommandHandler("consejo", consejo))
    dp.add_handler(telegram.ext.CommandHandler("dofollow", dofollow))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()