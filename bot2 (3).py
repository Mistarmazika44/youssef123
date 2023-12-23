import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '6934288216:AAHd329OTFV_99KsYxQM6G3A3sOcwRVn5xo'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber ='6649298332'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == subscriber:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ JOIN ✨", url="https://t.me/Mohamed891846")
		keyboard.add(contact_button)
	
		bot.send_message(chat_id=message.chat.id, text='''Sorry, you do not have a subscription to this bot. You can join the updates channel through the button below the message ''',reply_markup=keyboard)
		return
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text="✨ JOIN ✨", url="https://t.me/Mohamed891846")
	keyboard.add(contact_button)
	
	bot.send_message(chat_id=message.chat.id, text='''Send the file you want to check
	
Join the bot's updates channel now through the button below 💸 ''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == subscriber:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ JOIN ✨", url="https://t.me/Mohamed891846")
		keyboard.add(contact_button)
	
		bot.send_message(chat_id=message.chat.id, text='''Sorry, you do not have a subscription to this bot. You can join the updates channel through the button below the message ''',reply_markup=keyboard)
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Mistar_mazika18')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6934288216:AAHd329OTFV_99KsYxQM6G3A3sOcwRVn5xo]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(Tele(cc))
					print(cc,last)
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u6649298332')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u6649298332')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				contact_button = types.InlineKeyboardButton(text="👤 Help 👤", url="https://t.me/Mohamed891846")
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop,contact_button)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @MNOW4 ''', reply_markup=mes)
				if 'authenticate_attempt_successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
					vbv='𝗣𝗮𝘀𝘀𝗲𝗱 ✅'
				else:
					vbv='𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Approved
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑩𝑹𝑨𝑰𝑵𝑻𝑹𝑬𝑬 𝑨𝑼𝑻𝑯
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀 : @THE_S7
◆ 𝑽𝑩𝑽 : {vbv}'''
				
				if "Approved" in last or 'Funds' in last:
					live += 1
					bot.reply_to(message, msg)
				else:
					dd += 1
				time.sleep(20.1)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
@bot.message_handler(commands=["chk"])
def start(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
	try:
		cc=message.text.replace('/chk ', '')
	except:
		bot.reply_to(message, "Wrong format ❌")
		return
	try:
		data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
	except:
		pass
	try:
		bank=(data['bank']['name'])
	except:
				bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		emj=(data['country']['emoji'])
	except:
				emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		cn=(data['country']['name'])
	except:
				cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		dicr=(data['scheme'])
	except:
				dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		typ=(data['type'])
	except:
				typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		url=(data['bank']['url'])
	except:
		url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		last = str(Tele(cc))
	except Exception as e:
		print(e)
		last='ERROR'
		
	if "live" in last or 'Funds' in last:
		live += 1
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code> 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑩𝑹𝑨𝑰𝑵𝑻𝑹𝑬𝑬 𝑨𝑼𝑻𝑯
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	elif 'successfully' in last:
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑩𝑹𝑨𝑰𝑵𝑻𝑹𝑬𝑬 𝑨𝑼𝑻𝑯
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	else:
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code> 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝐷𝐸𝐶𝐿𝐼𝑁𝐸𝐷 ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑩𝑹𝑨𝑰𝑵𝑻𝑹𝑬𝑬 𝑨𝑼𝑻𝑯
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
print("تم تشغيل البوت")
bot.polling()
