from pyrogram import Client, filters
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
import re
from deep_translator import GoogleTranslator
import pymysql
from config import sockdata


translator = GoogleTranslator(source='auto', target='ru')


load_dotenv(join(dirname(__file__), '.env'))

botTG = Client(environ.get('APP_NAME'), api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'))



params: dict = {
	
	'test': -1001651474042,
	'test2': -1001651474042,
	'target_chat_id': -1001461338272


}


class Messages:
	def __init__(self):
		self.connection = pymysql.connect(**sockdata)
		self.cursor = self.connection.cursor()



	def add_to_vipclub(self, message_id: int, message_text: str):
		try:
			with self.connection as connect:
				self.cursor.executemany("INSERT INTO vipclub (message_id, message_text) VALUES (%s, %s);", message.id, translate_channel2)
				connect.commit()
				if pymysql.err.errno == 1205:
					print("Timeout error")
				else:
					raise
		except pymysql.err.OperationalError:
			print("Can't execute fron database vipclub")
			if self.connection.is_connected():
				connection.close()
		finally:
			time.sleep(4)


	def add_to_vipfuture(self, message_id: int, message_text: str):
		try:
			with self.connection as connect:
				self.cursor.executemany("INSERT INTO vipfuture (message_id, message_text) VALUES (%s, %s);", message.id, translate_channel1)
				connect.commit()
				if pymysql.err.errno == 1205:
					print("Timeout error")
				else:
					raise
		except pymysql.err.OperationalError:
			print("Can't execute fron database vipfuture")
			if self.connection.is_connected():
				connection.close()

		finally:
			time.sleep(4)


	def exists(self):
		pass


# @botTG.on_message(filters.chat(params['test']))
# async def sending_message(client, message):
# 	global translator
# 	text: str = ""
# 	eng_check = re.compile(r'[A-za-z0-9]')
# 	text = "".join(message.text)
# 	translate_channel1 = translator.translate(text)
# 	print(type(translate_channel1))
# 	with botTG:
# 		await botTG.forward_messages(params['target_chat_id'], params['test'], message.id, message.text) #сюда надо в параметры закидывать в цикле
		


async def send_clear(text):
	with botTG:
		await botTG.send_message(params['target_chat_id'], text)


async def send_clear(text):
	with botTG:
		await botTG.send_message(params['target_chat_id'], text)


@botTG.on_message(filters.chat(params['test2']))
async def sending_message2(client, message):
	text: str = ""
	
	text = "".join(message.text)
	text = text.replace("Entry Price:", "Цена входа:")
	text = text.replace("Take Profit", "Тейк профит")
	text = text.replace("Mark Price:", "Цена маркировки:")
	text = text.replace("Period:", "Период:")
	text = text.replace("Profit by signal:", "Прибыль по сигналу:")
	text = text.replace("(Short)", "Шорт")
	text = text.replace("Cross", "Кросс")
	text = text.replace("TP:", "Тейк Профит:")
	text = text.replace("SL:", "Стоп Лосс:")
	text = text.replace("Entry Targets:", "Точка входа:")
	
	print(text)
	await send_clear(text)

botTG.run()