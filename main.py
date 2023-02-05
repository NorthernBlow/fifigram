from pyrogram import Client, filters
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
import re

load_dotenv(join(dirname(__file__), '.env'))

botTG = Client(environ.get('APP_NAME'), api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'))



params: dict = {
	
	'vip_future': -1001552023060,
	'vip_club': -1001756092613,
	'target_chat_id': -1001522615061


}


@botTG.on_message(filters.chat(params['vip_future']))
async def sending_message(client, message):
	text: str = ""
	eng_check = re.compile(r'[A-za-z0-9]')
	text = "".join(message.text)
	print(type(text))
	with botTG:
		await botTG.forward_messages(params['target_chat_id'], params['vip_future'], message.id, message.text) #сюда надо в параметры закидывать в цикле
		


@botTG.on_message(filters.chat(params['vip_club']))
async def sending_message(client, message):
	text: str = ""
	eng_check = re.compile(r'[A-za-z0-9]')
	text = "".join(message.text)
	print(type(text))
	with botTG:
		await botTG.forward_messages(params['target_chat_id'], params['vip_club'], message.id, message.text)


botTG.run()