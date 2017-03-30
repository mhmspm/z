#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import demjson as json
from telebot import util,types
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


api = "376503635:AAGqdCmnOIq-Hg6BYJUo6_kXjQ1F-iA7BTc"
helper = telebot.TeleBot(api)
sudo = [114042404]

def load_data(filename):
	f = open(filename)
	if not f:
		return
	s = f.read()
	data = json.decode(s)
	return data
	
def save_data(filename, data):
	s = json.encode(data)
	f = open(filename, 'w')
	f.write(s)
	f.close()

dos = "moderation.json"
data = load_data("moderation.json")

@helper.message_handler(commands=['start', 'setting'])
def starting(msg):
	markup = types.InlineKeyboardMarkup()
	a = types.InlineKeyboardButton("تنظیمات اصلی 🔩", callback_data='Setting')   
	b = types.InlineKeyboardButton("تنظیمات رسانه ای 🔩", callback_data='Mutes')  
	markup.add(a, b)
	c = types.InlineKeyboardButton("درباره ما", callback_data='about')  
	markup.add(c)
	helper.send_message(msg.chat.id, "به ربات هلپر خوش آمدید", reply_markup=markup)

@helper.callback_query_handler(func=lambda call: True)
def inline(call):
	try:
	############
	# Setting  #
	############

		bot = data[str(call.message.chat.id)]["settings"]["lock_bots"]
		mark = data[str(call.message.chat.id)]["settings"]["lock_markdown"]
		spam = data[str(call.message.chat.id)]["settings"]["lock_spam"]
		web = data[str(call.message.chat.id)]["settings"]["lock_webpage"]
		link = data[str(call.message.chat.id)]["settings"]["lock_link"]
		flood = data[str(call.message.chat.id)]["settings"]["flood"]
		tag = data[str(call.message.chat.id)]["settings"]["lock_tag"]
		owner = data[str(call.message.chat.id)]["owners"]
		mods = data[str(call.message.chat.id)]["mods"]

	############
	#  Mutes   #
	############

		audio = data[str(call.message.chat.id)]["mutes"]["mute_audio"]
		contact = data[str(call.message.chat.id)]["mutes"]["mute_contact"]
		doc = data[str(call.message.chat.id)]["mutes"]["mute_doc"]
		fwd = data[str(call.message.chat.id)]["mutes"]["mute_fwd"]
		gif = data[str(call.message.chat.id)]["mutes"]["mute_gif"]
		loc = data[str(call.message.chat.id)]["mutes"]["mute_loc"]
		photo = data[str(call.message.chat.id)]["mutes"]["mute_photos"]
		video = data[str(call.message.chat.id)]["mutes"]["mute_video"]
		alls = data[str(call.message.chat.id)]["mutes"]["mute_all"]

		if call.message:

			if call.data == "Setting":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					markup = types.InlineKeyboardMarkup()
					a = types.InlineKeyboardButton("Bot", callback_data='1')  
					b = types.InlineKeyboardButton(str(bot), callback_data='boting')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Markdown", callback_data='1')  
					b = types.InlineKeyboardButton(str(mark), callback_data='marking')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Spam", callback_data='1')  
					b = types.InlineKeyboardButton(str(spam), callback_data='spaming')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Web", callback_data='1')  
					b = types.InlineKeyboardButton(str(web), callback_data='webing')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Link", callback_data='1')  
					b = types.InlineKeyboardButton(str(link), callback_data='linking')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Flood", callback_data='1')  
					b = types.InlineKeyboardButton(str(flood), callback_data='flooding')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Tag", callback_data='1')  
					b = types.InlineKeyboardButton(str(tag), callback_data='taging')
					markup.add(a, b)
					helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="تنظیمات گروه شما‌",reply_markup=markup)
				else:
					bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="شما اجازه دسترسی به تنظیمات را ندارید")
			if call.data == "boting":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if bot == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_bots"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ورود ربات غیرفعال شد",reply_markup=markup)
					elif bot == "no":
						data[str(call.message.chat.id)]["settings"]["lock_bots"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ورود ربات فعال شد",reply_markup=markup)

			if call.data == "marking":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if mark == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_markdown"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل حروف مارک و Html غیر فعال شد",reply_markup=markup)
					elif mark == "no":
						data[str(call.message.chat.id)]["settings"]["lock_markdown"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل حروف مارک و Html فعال شد",reply_markup=markup)

			if call.data == "spaming":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if spam == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_spam"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل پیام های بلند و خرابکارانه غیرفعال شد ",reply_markup=markup)
					elif spam == "no":
						data[str(call.message.chat.id)]["settings"]["lock_spam"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل پیام های بلند و خرابکارانه فعال شدشد",reply_markup=markup)


			if call.data == "webing":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if web == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_webpage"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال ادرس صفحات وب غیرفعال شد",reply_markup=markup)
					elif web == "no":
						data[str(call.message.chat.id)]["settings"]["lock_webpage"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال ادرس صفحات وب فعال شد",reply_markup=markup)


			if call.data == "linking":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if link == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_link"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال لینک غیرفعال شد",reply_markup=markup)
					elif link == "no":
						data[str(call.message.chat.id)]["settings"]["lock_link"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال لینک فعال شد",reply_markup=markup)

			if call.data == "flooding":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if flood == "yes":
						data[str(call.message.chat.id)]["settings"]["flood"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال پیام های مکرر غیرفعال شد",reply_markup=markup)
					elif flood == "no":
						data[str(call.message.chat.id)]["settings"]["flood"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال پیام های مکرر فعال شد",reply_markup=markup)

			if call.data == "taging":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if tag == "yes":
						data[str(call.message.chat.id)]["settings"]["lock_tag"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال تگ غیرفعال شد",reply_markup=markup)
					elif tag == "no":
						data[str(call.message.chat.id)]["settings"]["lock_tag"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Setting') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال تگ فعال شد",reply_markup=markup)

	###########
	#  Mutes  #
	###########


			if call.data == "Mutes":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					markup = types.InlineKeyboardMarkup()
					a = types.InlineKeyboardButton("Audio", callback_data='1')  
					b = types.InlineKeyboardButton(str(audio), callback_data='auding')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Contact", callback_data='1')  
					b = types.InlineKeyboardButton(str(contact), callback_data='contacting')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Document", callback_data='1')  
					b = types.InlineKeyboardButton(str(doc), callback_data='documentig')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Forward", callback_data='1')  
					b = types.InlineKeyboardButton(str(fwd), callback_data='fwding')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Gif", callback_data='1')  
					b = types.InlineKeyboardButton(str(gif), callback_data='gifing')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Location", callback_data='1')  
					b = types.InlineKeyboardButton(str(loc), callback_data='locating')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Photo", callback_data='1')  
					b = types.InlineKeyboardButton(str(photo), callback_data='photing')
					markup.add(a, b)
					a = types.InlineKeyboardButton("Video", callback_data='1')  
					b = types.InlineKeyboardButton(str(video), callback_data='videing')
					markup.add(a, b)
					a = types.InlineKeyboardButton("All", callback_data='1')  
					b = types.InlineKeyboardButton(str(alls), callback_data='alling')
					markup.add(a, b)
					helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="تنظیمات رسانه ای گروه شما",reply_markup=markup)
				else:
					bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="شما اجازه دسترسی به تنظیمات را ندارید")




			if call.data == "auding":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if audio == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_audio"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل صدا غیرفعال شد",reply_markup=markup)
					elif audio == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_audio"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل صدا فعال شد",reply_markup=markup)

			if call.data == "contacting":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if contact == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_contact"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال شماره غیرفعال شد",reply_markup=markup)
					elif contact == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_contact"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال شماره فعال شد",reply_markup=markup)

			if call.data == "documentig":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if doc == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_doc"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال فایل غیرفعال شد",reply_markup=markup)
					elif doc == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_doc"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال فایل فعال شد",reply_markup=markup)


			if call.data == "fwding":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if fwd == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_fwd"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل فروارد غیرفعال شد",reply_markup=markup)
					elif fwd == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_fwd"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل فروارد فعال شد",reply_markup=markup)


			if call.data == "gifing":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if gif == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_gif"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال گیف غیرفعال شد",reply_markup=markup)
					elif gif == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_gif"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال گیف فعال شد",reply_markup=markup)

			if call.data == "locating":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if loc == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_loc"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال مکان غیرفعال شد",reply_markup=markup)
					elif loc == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_loc"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال مکان فعال شد",reply_markup=markup)

			if call.data == "photing":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if photo == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_photos"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال عکس غیرفعال شد",reply_markup=markup)
					elif photo == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_photos"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال عکس فعال شد",reply_markup=markup)

			if call.data == "videing":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if video == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_video"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال فیلم غیرفعال شد",reply_markup=markup)
					elif video == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_video"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل ارسال فیلم فعال شد",reply_markup=markup)

			if call.data == "alling":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					if alls == "yes":
						data[str(call.message.chat.id)]["mutes"]["mute_all"] = "no"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 				
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل تمام تنظیمات رسانه ای غیرفعال شد",reply_markup=markup)
					elif alls == "no":
						data[str(call.message.chat.id)]["mutes"]["mute_all"] = "yes"
						save_data(dos, data)
						markup = types.InlineKeyboardMarkup()
						a = types.InlineKeyboardButton("Back", callback_data='Mutes') 			
						markup.add(a)
						helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قفل تمام تنظیمات رسانه ای فعال شد",reply_markup=markup)
			if call.data == "about":
				if str(call.from_user.id) in owner or str(call.from_user.id) in mods or call.from_user.id in sudo:
					helper.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" by aramesh")

	except Exception as e:
		helper.send_message(call.message.chat.id,"مشکلی وجود دارد\n\nقفل موردنظر خود را یک بار باز و بسته کنید تا درست شود")
		print e
helper.polling(True)
