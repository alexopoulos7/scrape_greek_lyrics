#!/usr/bin/python3
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

host = 'http://www.stixoi.info/'
url = 'http://www.stixoi.info/stixoi.php?info=Lyrics&act=lyricist&sort=alpha'

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
all_lyrics = ""
count_poems = 0
all_links = soup.find_all("a")
all_alpha_links = [l for l in all_links if
                   l.get('href').startswith('stixoi.php?info=Lyrics&sort=alpha&order=asc&act=lyricist&letter=')]
for link in all_alpha_links:
    letter_url = "{}{}".format(host, link.get("href"))
    letter_url = letter_url.split('lyricist&letter=')
    letter_url[1] = urllib.parse.quote(letter_url[1])
    letter_url = "lyricist&letter=".join(letter_url)
    print("For Letter: {} URL= {}".format(link.contents[0], letter_url))
    html_letter = urlopen(letter_url)
    soup_letter = BeautifulSoup(html_letter, 'lxml')
    all_links_letter = soup_letter.find_all("a")
    all_alpha_letter_links = [l for l in all_links_letter if l.get('href').startswith('stixoi.php?info=Lyrics&act=index&sort=alpha&lyricist_id=')]
    for songs_link in all_alpha_letter_links:
        songs_url = "{}{}".format(host, songs_link.get("href"))
        song_page = urlopen(songs_url)
        soup_songs = BeautifulSoup(song_page, "lxml")
        soup_songs_links = soup_songs.find_all('a')
        all_soup_songs_links = [l for l in soup_songs_links if l.get('href').startswith('stixoi.php?info=Lyrics&act=details&song_id=')]
        for song_url in all_soup_songs_links:
            song_url = "{}{}".format(host, song_url.get("href"))
            print("Song = {}".format(song_url))
            song_lyrics = urlopen(song_url)
            soup_lyrics = BeautifulSoup(song_lyrics, 'lxml')
            lyrics_list = [x.text for x in soup_lyrics.findAll("div", {"class": "lyrics"})]
            all_lyrics += "\r\n\n".join(lyrics_list)
            count_poems += 1
    with open('input/{}'.format(link.contents[0]), 'w+') as f:
        f.write((all_lyrics))
        all_lyrics = ''
# with open('input/lyrics.txt', 'w+') as fh:
#     fh.write(all_lyrics)

print("Read {} in total poems!".format(count_poems))