import requests 
from bs4 import BeautifulSoup

def find_playlist_info(url):	 
	
	#open with GET method 
	resp=requests.get(url) 
	
	#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page") 
	
		# we need a parser,Python built-in HTML parser is enough . 
		soup=BeautifulSoup(resp.text,'html.parser')

		# title of the playlist
		# print(soup.title.text)

		songs = list()
		for song in soup.find_all("a", "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):
        		songs.append(song)

		print(songs)

		return songs
		# SONG LINKS 
		#songLinks = list()
		#i = 1
		#for link in soup.findAll('a'):
		#	if (link.get('href').find("t=0s") != -1) :
        	#		i += 1
        	#		if i % 2 == 1 :
        	#			songLinks.append("youtube.com" + link.get('href')) #print("youtube.com" + link.get('href'))


	else: 
		print("Error") 

playlist_url = input("Enter the url of the youtube playlist :")	
find_playlist_info(playlist_url)

