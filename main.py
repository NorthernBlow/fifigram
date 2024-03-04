from pyrogram import Client, filters
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
import threading
from pyrogram.types import InputMediaPhoto


load_dotenv(join(dirname(__file__), '.env'))

botTG = Client(environ.get('APP_NAME'), api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'))



params: dict = {
	
	'vip_future': -1001552023060,
	'vip_club': -1001756092613,
	'target_chat_id': -1001522615061,
	'test2': -1001651474042

}
images_ids: list = []


async def send_with_reply(text: str, clear_reply_message):
	"""Функция-пересыльщик сообщений, на которые есть ответ. Пересылает
	обработанный в функции sending_message() message.text, пересылает этот текст
	ответом на полученный id

args: text - str, переведенный. idreply - int, id сообщения. 
"""

	#with botTG:
	async for message in botTG.search_messages(params['target_chat_id'], "#team_1 \n" + clear_reply_message):
		print(' need id: ', message.id)
		await botTG.send_message(params['target_chat_id'], "#team_1 \n" + text, reply_to_message_id=message.id)




async def send_with_reply2(text: str, clear_reply_message):
	"""Функция-пересыльщик сообщений, на которые есть ответ. Пересылает
	обработанный в функции sending_message() message.text, пересылает этот текст
	ответом на полученный id

args: text - str, переведенный. idreply - int, id сообщения. 
"""

	#with botTG:
	async for message in botTG.search_messages(params['target_chat_id'], "#team_2 \n" + clear_reply_message):
		print(' need id: ', message.id)
		await botTG.send_message(params['target_chat_id'], "#team_2 \n" + text, reply_to_message_id=message.id)



async def send_clear(text):
	"""Функция-пересыльщик переведенных сообщений. Просто берет и пересылает
	обработанный в функции sending_message2() message.text

args: text - str, переведенный.
"""
	with botTG:
		await botTG.send_message(params['target_chat_id'], "#team_1 \n" + text)




async def send_clear2(text: str):
	"""Функция-пересыльщик переведенных сообщений. Просто берет и пересылает
	обработанный в функции sending_message() message.text

args: text - str, переведенный.
"""
	with botTG:
		await botTG.send_message(params['target_chat_id'], "#team_2 \n" + text)




def send_with_picture(images_ids):
	"""Функция-пересыльщик сообщений с фото. Пересылает
	фотографию с описанием в функции sending_message()

args: message - объект класса pyrogram.Client.Message
"""
	# with botTG:
	# print(message)

	# if not message.caption:
	# 	await botTG.send_cached_media(params['target_chat_id'], message.photo.file_id)
	# else:
	# 	await botTG.send_cached_media(params['target_chat_id'], message.photo.file_id, message.caption)

	if len(images_ids) > 0:
		botTG.send_media_group(params['target_chat_id'], images_ids)
		images_ids.clear() #занулил айдишники

	# print("send_with_reply OKAY :)")
	# print("images ids = ", images_ids)
	threading.Timer(6.0, send_with_picture, [images_ids]).start()
	return True




print('\033[91m' + "    I'm be back!" + '\033[0m')
threading.Timer(6.0, send_with_picture, [images_ids]).start()




@botTG.on_message(filters.chat(params['vip_club']))
async def sending_message(client, message):
	
	try:
		text: str = ""
		text = "".join(message.text)
		text = text.replace("Exchanges:", "Обмен:")
		text = text.replace("Signal Type:", "Тип сигнала:")
		text = text.replace("Leverage:", "Плечо:")
		text = text.replace("Entry Price:", "Цена входа:")
		text = text.replace("Take-Profit Targets:", "Цели:")
		text = text.replace("Entry Targets:", "Цена входа:")
		text = text.replace("Stop Targets:", "Стоп-лосс:")
		text = text.replace("Regular (Short)", "Стандартный (Шорт)")
		text = text.replace("Regular (Long)", "Стандартный (Лонг)")
		text = text.replace("Target", "Цель")
		text = text.replace("Mark Price", "Цена Маркировки")
		text = text.replace("Profit", "Профит")
		text = text.replace("achieved in", "достигнута в")
		
		
		
	except TypeError:
		print(' Здесь какая-то ошибка! СУКАА \n', TypeError)
		# if message:
		# 	if not message.photo:
		# 		try:
		# 			if message.reply_to_message_id:
		# 				pass
		# 				idreply = message.reply_to_message.id
		# 				await send_with_reply(text, idreply)
		# 		except AttributeError:
		# 			await send_clear2(text)
			
		# 	else: 
		# 		print("Это эсепшин ------------------>\n\n\n", message)
		# 		await send_with_picture(message)
	finally:
		# print("Это finally ------------------>\n\n\n", message)
		if message:
			if not message.photo:
				try:
					if message.reply_to_message_id:
						# print('this code.')
						chat_id = message.chat.id
						idreply = message.reply_to_message_id
						for_reply_message = await botTG.get_messages(chat_id, idreply)
						clear_reply_message = "".join(for_reply_message.text)
						clear_reply_message = clear_reply_message.replace("Exchanges:", "Обмен:")
						clear_reply_message = clear_reply_message.replace("Signal Type:", "Тип сигнала:")
						clear_reply_message = clear_reply_message.replace("Leverage:", "Плечо:")
						clear_reply_message = clear_reply_message.replace("Entry Price:", "Цена входа:")
						clear_reply_message = clear_reply_message.replace("Take-Profit Targets:", "Цели:")
						clear_reply_message = clear_reply_message.replace("Entry Targets:", "Цена входа:")
						clear_reply_message = clear_reply_message.replace("Stop Targets:", "Стоп-лосс:")
						clear_reply_message = clear_reply_message.replace("Regular (Short)", "Стандартный (Шорт)")
						clear_reply_message = clear_reply_message.replace("Regular (Long)", "Стандартный (Лонг)")


						clear_reply_message = clear_reply_message.replace("Target", "Цель")
						clear_reply_message = clear_reply_message.replace("Mark Price", "Цена Маркировки")
						clear_reply_message = clear_reply_message.replace("Profit", "Профит")
						clear_reply_message = clear_reply_message.replace("achieved in", "достигнута в")
						print(for_reply_message.text)
						# print('Ok?')
						await send_with_reply(text, clear_reply_message)
					else:
						await send_clear(text)
				except AttributeError as ae:
					print(' Здесь какая-то ошибка! СУКАА \n', ae)
					await send_clear(text)
			
			#else:
				#images_ids.append(InputMediaPhoto(message.photo.file_id, caption=message.caption))
				# print("images ids = ", images_ids)
				# await send_with_picture(message)
				






@botTG.on_message(filters.chat(params['vip_future']))
async def sending_message2(client, message):
	try:
		text: str = ""
		
		text = "".join(message.text)
		
		text = text.replace("Take Profit", "Тейк профит")
		text = text.replace("Mark Price:", "Цена маркировки:")
		text = text.replace("Period:", "Период:")
		text = text.replace("Profit by signal:", "Прибыль по сигналу:")
		text = text.replace("(Short)", "Шорт")
		text = text.replace("Cross", "Плечо")
		text = text.replace("TP:", "Тейк Профит:")
		text = text.replace("SL:", "Стоп Лосс:")
		text = text.replace("Entry Targets:", "Точка входа:")
		text = text.replace("(Long)", "Лонг")
		text = text.replace("Entry Price:", "Цена входа:")


		#new

		text = text.replace("Target", "Цель")
		text = text.replace("Mark Price", "Цена Маркировки")
		text = text.replace("Profit", "Профит")
		
		


	except TypeError:
		print(' Здесь какая-то ошибка! СУКАА \n', TypeError)
		# if message:
		# 	if not message.photo:
		# 		try:
		# 			if message.reply_to_message_id:
		# 				pass
		# 				idreply = message.reply_to_message.id
		# 				await send_with_reply(text, idreply)
		# 		except AttributeError:
		# 			await send_clear(text)
			
		# 	else: 
		# 		await send_with_picture(message)
	finally:
		# print("Это finally ------------------>\n\n\n", message)
		if message:
			if not message.photo:
				try:
					if message.reply_to_message_id:
						# print('this code.')
						chat_id = message.chat.id
						idreply = message.reply_to_message_id
						for_reply_message = await botTG.get_messages(chat_id, idreply)
						clear_reply_message = "".join(for_reply_message.text)
		
						clear_reply_message = clear_reply_message.replace("Take Profit", "Тейк профит")
						clear_reply_message = clear_reply_message.replace("Mark Price:", "Цена маркировки:")
						clear_reply_message = clear_reply_message.replace("Period:", "Период:")
						clear_reply_message = clear_reply_message.replace("Profit by signal:", "Прибыль по сигналу:")
						clear_reply_message = clear_reply_message.replace("(Short)", "Шорт")
						clear_reply_message = clear_reply_message.replace("Cross", "Плечо")
						clear_reply_message = clear_reply_message.replace("TP:", "Тейк Профит:")
						clear_reply_message = clear_reply_message.replace("SL:", "Стоп Лосс:")
						clear_reply_message = clear_reply_message.replace("Entry Targets:", "Точка входа:")
						clear_reply_message = clear_reply_message.replace("(Long)", "Лонг")
						clear_reply_message = clear_reply_message.replace("Entry Price:", "Цена входа:")


						#new

						clear_reply_message = clear_reply_message.replace("Target", "Цель")
						clear_reply_message = clear_reply_message.replace("Mark Price", "Цена Маркировки")
						clear_reply_message = clear_reply_message.replace("Profit", "Профит")
						#print(for_reply_message)
						# print('Ok?')
						await send_with_reply2(text, clear_reply_message)
					else:
						await send_clear2(text)
				except AttributeError as ae:
					print(' Здесь какая-то ошибка! СУКАА \n', ae)
					await send_clear2(text)
			
			else:
				images_ids.append(InputMediaPhoto(message.photo.file_id, caption=message.caption))
				# print("images ids = ", images_ids)
				# await send_with_picture(message)


# FIXME: если надо запустить бота, надо закомментить работу с выгрузкой истории. 
# async def history():
# 	dump: str = ''
# 	async with botTG:
# 		with open('dump.txt', 'w') as f:
# 			async for message in botTG.get_chat_history(params['vip_future']):
# 				dump += message.text + '\n' + str(message.date)
				
# 				f.write(dump)
# 				f.write('\n')
# 				print(message)


# async def main():
# 	task = asyncio.create_task(history())
# 	await task


# asyncio.run(main())
botTG.run()
