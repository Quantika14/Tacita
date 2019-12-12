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
from apk_parse.apk import APK
from pymongo import MongoClient
import os, re, time
from os import listdir

#import modules.idiomas_detector as ID

class colores:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    alert = '\033[93m'
    fail = '\033[91m'
    normal = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

client = MongoClient()
db = client.Tacita
start = 100000
end = 110000

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
	print "Name app: Tacita-APKanalyze.py"
  	print "****************************"
	print "- The last version 12/12/2019"

def insert_mongodb(id_file, package, md5, file_size, andro_version, main_activity, activities, services, permissions, urls, emails, ftps, IPs, strings):
	global client, db

	try:
		cursor = db.Tacita.find({"id_file":id_file})
		if cursor:
			
			date_Insert = time.strftime("%c")
			date_Update = "none"
			cursor = db.Tacita.update({"id_file":id_file},{"id_file": id_file, "package": package, "file_md5": md5, "file_size": file_size, "AndroidVersion": andro_version,"main_activity": main_activity, "activities": activities, "services": services, "permissions": permissions, "links": urls, "emails": emails, "ftps": ftps, "ips": IPs, "strings": strings, "date_Insert": date_Insert, "date_Update": date_Update, "bot":"DownloadAPK"})
			print colores.blue + "[INFO][>] UPDATE IN DB" + colores.normal
		else:
			date_Insert = time.strftime("%c")
			date_Update = "none"
			cursor = db.Tacita.insert({"id_file": id_file, "package": package, "file_md5": md5, "file_size": file_size, "AndroidVersion": andro_version,"main_activity": main_activity, "activities": activities, "services": services, "permissions": permissions, "links": urls, "emails": emails, "ftps": ftps, "ips": IPs, "strings": strings, "date_Insert": date_Insert, "date_Update": date_Update, "bot":"DownloadAPK"})
			print colores.blue + "[INFO][>] INSERT IN DB" + colores.normal

	except Exception as e:
		print e
		pass


def ls(ruta = 'bot'):
    return listdir(ruta)

def main():
	banner()
	for target in ls():
		target = "bot/" + str(target)

		apkf = APK(target)

		md5 = apkf.file_md5
		package = apkf.get_package()
		file_size = apkf.file_size
		andro_version = apkf.get_androidversion_name()
		libraries = apkf.get_libraries()
		main_activity = apkf.get_main_activity()
		activities = apkf.get_activities()
		services = apkf.get_services()
		files = apkf.get_files()
		permissions = apkf.get_permissions()

		counter_emails = 0
		counter_urls = 0
		counter_ftps = 0

		all_emails = []
		all_urls = []
		all_ftps = []
		all_ips = []
		all_words = []

		print "----------------------------------------------"
		print colores.underline + "[+][TARGET][>]" + str(package) + " ["+ str(target) +"]" +  colores.normal
		print colores.header + "[-][md5][>] " + md5 
		print colores.header + "[-][Android version][>] " + andro_version
		print colores.green + "|----[>] " + "Searching emails, links, FTP and IPs in strings ..." + colores.normal

		#Strings
		strings = os.popen("strings " + target) 

		for word in strings:
			#Save word in array
			all_words.append(word)

			#To found emails in strings
			if "@" in word:
				try:
					if word.find(".com")>0 or word.find(".es")>0 or word.find(".eu")>0 or word.find(".net")>0 or word.find(".gob")>0 or word.find(".info")>0 or word.find(".org")>0:
						words = word.split(" ")
						for w in words:
							if word.find(".com")>0 or word.find(".es")>0 or word.find(".eu")>0 or word.find(".net")>0 or word.find(".gob")>0 or word.find(".info")>0 or word.find(".org")>0:
								counter_emails += 1
								email = re.findall(r'[\w\.-]+@[\w\.-]+', word)
								if not email in all_emails:
									print(colores.green + "|----[EMAIL][>] " + str(email) + colores.normal)
									all_emails.append(email)
				except Exception as e:
					print e
			#To found urls in strings
			if "http" in word or "wwww." in word:
				try:
					url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word)
					if not url in all_urls or url == "":
						all_urls.append(url)
						print colores.green + "|----[URL][>] " + str(url) + colores.normal
				except Exception as e:
					print e

			#To found FTP in strings
			if "ftp" in word:
				try:
					ftp = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word)
					if not ftp in all_ftps or ftp == "":
						all_ftps.append(ftp)
						print colores.green + "|----[FTP][>] " + str(ftp) + colores.normal
				except Exception as e:
					print e
				
			#Find IP in strings
			ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', word)
			if ip:
				try:
					all_ips.append(ip)
					print colores.green + "|----[IP][>] " + str(ip) + colores.normal
				except Exception as e:
					print e
			

		#Save in DB
		insert_mongodb(target, package, md5, file_size, andro_version, main_activity, activities, services, permissions, all_urls, all_emails, all_ftps, all_ips, all_words)
				



if __name__ == "__main__":
	main()
