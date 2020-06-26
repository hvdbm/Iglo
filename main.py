import requests 
from bs4 import BeautifulSoup

class Playlist:
    def __init__(self, songs, contributors):
        self.songs = songs
        self.contributors = contributors

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
    i = 0
    while i < len(playlist.contributors):
		    line = playlist.songs[i].text[7:-5] + ' ajouté par ' + playlist.contributors[i] + '\n'
		    i += 1
		    file.write(line)
    file.close()
    print("playlist.txt has been generated \n")

def write_txt_sheets(playlist):
	file = open("playlist.txt", "w")
	for song in playlist.songs:
    		songName = song.text[7:-5].replace('"', '')		# must supress any " for Google Sheets
    		line = '=HYPERLINK("https://youtube.com' + song.get('href') + '"; "' + songName + '") \n'
    		file.write(line)
	file.close()
	print("playlist.txt has been generated \n")

def choose_option(playlist):
        print("What format do you want to use ? \n 1- Default \n 2- Google Sheets")
        option = input("Choose a writing option: ")
        if option == '1': write_txt(playlist)
        elif option == '2': write_txt_sheets(playlist)

playlist = Playlist(list(), list())
playlistUrl = input("Enter the url of the youtube playlist: ")

find_playlist_info(playlistUrl, playlist)
choose_option(playlist)