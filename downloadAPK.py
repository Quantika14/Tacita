#!/usr/bin/python
#-*- coding:utf-8 -*-
''' 
Copyright (C) 2016  QuantiKa14 Servicios Integrales S.L
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from urllib.request import urlretrieve,urlcleanup
from apk_parse.apk import APK
import cfscrape
import time, os
import magic

count_apk = 0
count_html = 0
start = 100000
end = 100005

def new_dir():
	ruta = r'bot' 
	if not os.path.exists(ruta): os.makedirs(ruta)
	return True

def banner():
	print("---------|||     |||--------")
	print("---------|||     |||--------")
	print("---------|||     ||||||||---")
	print("---------|||     |||---||---")
	print("---------|||     |||---||---")
	print("---------|||     ||||||||---")
	print("---------|||||||||||--------")
	print("****************************")
	print("little-cup.py | QuantiKa14")
	print("Author: Jorge Websec")
	print("Bot: DownloadAPK.py")
	print("****************************")
	
	
def download(url, file_name, scraper):
	with open(file_name, "wb") as file:
		try:
			response = scraper.get(url, allow_redirects=True)
			file.write(response.content)
		except HTTPError as http_err:
			print(f'HTTP error occurred: {http_err}')
		except Exception as ex:
			print(ex)

def main():
	global count_apk, count_html, start, end

	banner()
	if new_dir:
		print ("[INFO] check dir 'bot'...")
		os.chdir('bot')

	enlapsed_time = (end - start)/60
	print ("[INFO] Estimated time: " + str(enlapsed_time) + "min")
	
	scraper = cfscrape.create_scraper()

	for i in range(start, end):
		try:
			url = ("https://www.apkmirror.com/wp-content/themes/APKMirror/download.php?id=" + str(i))
			filename = str(i)
			download(url, filename, scraper)
			time.sleep(1)
		except Exception as ex:
			print(ex)
	for i in range(start, end):
		file_type = magic.from_file(str(i))

		if file_type.find('HTML document')>0:
			count_html +=1
		else:
			count_apk += 1
	print("[INFO] " + str(count_html) + " html downloaded...")
	print ("[INFO] " + str(count_apk) + " apks downloaded...")

if __name__ == "__main__":
	main()
