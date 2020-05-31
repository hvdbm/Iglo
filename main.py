import requests 
from bs4 import BeautifulSoup

def write_txt(songs):
	file = open("playlist.txt", "w")
	for song in songs:
    		songName = song.text[7:-5].replace('"', '')		# must supress any " for Google Sheets
    		line = '=HYPERLINK("https://youtube.com' + song.get('href') + '"; "' + songName + '") \n'
    		file.write(line)
	file.close()
	print("playlist.txt has been generated \n")

def find_playlist_info(url):	 
	#open with GET method 
	resp=requests.get(url) 
	
	#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page \n") 
	
		# we need a parser,Python built-in HTML parser is enough . 
		soup=BeautifulSoup(resp.text,'html.parser')

		songs = list()
		for song in soup.find_all("a", "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):
        		songs.append(song)
		
		#contributors = list()
		#for contributor in soup.find_all("a"):
        		#if contributor.get('aria-label') != None : contributors.append(contributor.get('aria-label')[0:-7])
		#print(contributors)
		return songs

	else: 
		print("Error. Can't open the web page") 

playlistUrl = input("Enter the url of the youtube playlist: ")
write_txt(find_playlist_info(playlistUrl))
