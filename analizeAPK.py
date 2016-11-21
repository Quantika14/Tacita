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
from urllib import urlretrieve, urlcleanup
from apk_parse.apk import APK
from requests import get
import time, os

count_apk = 0
count_html = 0
#start < end
start = 100000 #<-- cambiar
end = 110000 #<-- cambiar

def new_dir():
	ruta = r'bot' 
	if not os.path.exists(ruta): os.makedirs(ruta)
	return True

def banner():
	print "---------|||     |||--------"
	print "---------|||     |||--------"
	print "---------|||     ||||||||---"
	print "---------|||     |||---||---"
	print "---------|||     |||---||---"
	print "---------|||     ||||||||---"
	print "---------|||||||||||--------"
	print "****************************"
	print "little-cup.py | QuantiKa14"
	print "Author: Jorge Websec"
	print "Bot: DownloadAPK.py"

def download(url, file_name):
	with open(file_name, "wb") as file:
		try:
			response = get(url, allow_redirects=True)
			file.write(response.content)
		except:
			pass

def main():
	global count_apk, count_html, start, end

	banner()
	if new_dir:
		print "[INFO] check dir 'bot'..."
		os.chdir('bot')

	time = (end - start)/60
	print "[INFO] Estimated time: " + str(time) + "min"

	for i in range(start, end):
		try:
			url = ("http://www.apkmirror.com/wp-content/themes/APKMirror/download.php?id=" + str(i))
			filename = str(i)
			download(url, filename)
			time.sleep(1)
		except:
			continue
	for i in range(start, end):
		f = open(str(i), 'r')
		if f.readline().find('html')>0:
			count_html +=1
		else:
			count_apk += 1
		f.close()
	print "[INFO] " + str(count_html) + " html downloaded..."
	print "[INFO] " + str(count_apk) + " apks downloaded..."

if __name__ == "__main__":
	main()
