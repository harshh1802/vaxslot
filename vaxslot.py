import requests
import telegram_send
import time
import pyautogui


pincode = pyautogui.prompt('Enter the pincode')
date = pyautogui.prompt('Enter the Date in DD-MM-YYYY format')



# pincode = 395004
# date = '31-08-2021'
base = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,date)
list = []

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def check():
	counter = 0
	page = requests.get(base)
	page_json = page.json()
	data = page_json['sessions']
	# res = len([ele for ele in data if isinstance(ele, dict)])

	for i in data:
		name = i['name']
		address = i['address']
		dose1 = i['available_capacity_dose1']
		dose2 = i['available_capacity_dose2']
		doseboth = i['available_capacity']

		if ((i['available_capacity'] > 0) & (i['fee_type'] == 'Free')):
			msg = 'Hey, I found slot.\n {}\n {}\n Dose 1:{}\n Dose 2:{}'.format(name,address,dose1,dose2)
			counter += 1
			telegram_send.send(messages=[msg])
			return True

	if counter == 0:
		print('No slot available!')
		return False


while (check() !=  True):
	check()
	time.sleep(60)








	




