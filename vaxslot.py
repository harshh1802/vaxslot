import requests
import telegram_send
import time
from datetime import datetime , timedelta




pincode = 395004
present_day = datetime.now()
next_day = datetime.now() + timedelta(1)
date = [present_day.strftime("%d-%m-%y"),next_day.strftime("%d-%m-%y")]



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def check():
	for d in date:
		base = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,d)
		counter = 0
		page = requests.get(base)
		page_json = page.json()
		data = page_json['sessions']



	# Katargam community hall : 709997
	# samast patidar samaj vadi : 711599



		for i in data:
			name = i['name']
			center = i['center_id']
			address = i['address']
			dose1 = i['available_capacity_dose1']
			dose2 = i['available_capacity_dose2']
			doseboth = i['available_capacity']

			if ((doseboth > 0) & (center == 711599) ):
				msg = 'Hey, I found slot.\n {}\n {}\n Dose 1:{}\n Dose 2:{}'.format(name,address,dose1,dose2)
				counter += 1
				telegram_send.send(messages=[msg])
				return True

		if counter == 0:
			print('No slot available! for {}'.format(d))
			# return False


while (check() !=  True):
	check()
	time.sleep(60)








	





