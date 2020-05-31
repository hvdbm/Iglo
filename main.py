import requests 
from bs4 import BeautifulSoup

def write_txt(songs):
	file = open("playlist.txt", "w")
	for song in songs:
    		line = '=HYPERLINK("https://youtube.com' + song.get('href') + '"; "' + song.text[7:-6] + '") \n'
    		file.write(line)
	file.close()

def find_playlist_info(url):	 
	
	#open with GET method 
	resp=requests.get(url) 
	
	#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page") 
	
		# we need a parser,Python built-in HTML parser is enough . 
		soup=BeautifulSoup(resp.text,'html.parser')

		songs = list()
		for song in soup.find_all("a", "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):
        		songs.append(song)

		#print(songs)

		return songs

	else: 
		print("Error. Can't open the web page") 

playlist_url = input("Enter the url of the youtube playlist: ")
write_txt(find_playlist_info(playlist_url))
