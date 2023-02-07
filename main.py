from pyrogram import Client, filters
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname



load_dotenv(join(dirname(__file__), '.env'))

botTG = Client(environ.get('APP_NAME'), api_id=environ.get('API_ID'), api_hash=environ.get('API_HASH'))



params: dict = {
	
	'vip_future': -1001552023060,
	'vip_club': -1001756092613,
	'target_chat_id': -1001522615061

}



async def send_clear2(text):
	with botTG:
		await botTG.send_message(params['target_chat_id'], text)




@botTG.on_message(filters.chat(params['vip_club']))
async def sending_message(client, message):
	
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
	await send_clear2(text)
		




async def send_clear(text):
	with botTG:
		await botTG.send_message(params['target_chat_id'], text)


@botTG.on_message(filters.chat(params['vip_future']))
async def sending_message2(client, message):
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
	
	print(text)
	await send_clear(text)

botTG.run()