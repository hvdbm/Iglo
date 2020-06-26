import requests 
from bs4 import BeautifulSoup

class Playlist:
    def __init__(self, songs, contributors):
        self.songs = songs
        self.contributors = contributors

#def write_txt_default
#def write_txt_sheets

#def find_playlist_name

def find_playlist_contributors(soup):
    contributors = list()
    for contributor in soup.find_all("a"):
        	if contributor.get('aria-label') != None : contributors.append(contributor.get('aria-label')[0:-7])
    return contributors

def find_playlist_songs(soup):
	songs = list()
	for song in soup.find_all("a", "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link"):
        	songs.append(song)
	return songs

def write_txt(playlist):
	file = open("playlist.txt", "w")
	for song in playlist.songs:
    		songName = song.text[7:-5].replace('"', '')		# must supress any " for Google Sheets
    		line = '=HYPERLINK("https://youtube.com' + song.get('href') + '"; "' + songName + '") \n'
    		file.write(line)
	file.close()
	print("playlist.txt has been generated \n")

def find_playlist_info(url, playlist):	 
	#open with GET method 
	resp=requests.get(url) 
	
	#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page \n") 
	
		# we need a parser,Python built-in HTML parser is enough . 
		soup=BeautifulSoup(resp.text,'html.parser')

		playlist.songs = find_playlist_songs(soup)
		playlist.contributors = find_playlist_contributors(soup)

	else: 
		print("Error. Can't open the web page") 

playlist = Playlist(list(), list())
playlistUrl = input("Enter the url of the youtube playlist: ")

find_playlist_info(playlistUrl, playlist)
write_txt(playlist)