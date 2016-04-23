import xml.etree.ElementTree as ET
import sqlite3

c=sqlite3.connect('tracks.sqlite')
cur=c.cursor()

cur.executescript('''CREATE TABLE IF NOT EXISTS Artist(
						id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						name TEXT UNIQUE
					);
					CREATE TABLE IF NOT EXISTS Album(
						id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						artist_id INTEGER,
						title TEXT UNIQUE
					);
					CREATE TABLE IF NOT EXISTS Genre (
                                            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            name    TEXT UNIQUE
                                        );

					CREATE TABLE IF NOT EXISTS Track(
						id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						album_id INTEGER,
						title TEXT UNIQUE,
						len INTEGER,
						count INTEGER,
						rating INTEGER,
						genre_id  INTEGER
					);
''')

fh="Library.xml"

def check(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

parsed_xml=ET.parse(fh)
al=parsed_xml.findall('dict/dict/dict')
for element in al :
	if (check(element,'Track ID') is None) :
		continue
	name=check(element,'Name')
	length=check(element,'Total Time')
	count=check(element,'Play Count')
	rating=check(element,'Rating')
	album=check(element,'Album')
	artist=check(element,'Artist')
	genre=check(element,'Genre')
	print name,length,count,rating,album,artist,genre
	if(album is None or artist is None or name is None or genre is None) :
		continue
	cur.execute('''		INSERT OR IGNORE INTO Artist(name) VALUES(?)''',(artist,))
	cur.execute('''SELECT id FROM Artist WHERE name=?''',(artist,))
	artist_id=cur.fetchone()[0]
	cur.execute('''INSERT OR IGNORE INTO Genre(name) VALUES(?)''',(genre,))
	cur.execute('''SELECT id FROM Genre WHERE name=?''',(genre,))
	genre_id=cur.fetchone()[0]
	cur.execute('''		INSERT OR IGNORE INTO Album(artist_id,title) VALUES(?,?)''',(artist_id,album))
	cur.execute(''' SELECT id FROM Album WHERE title=?''',(album,))
	album_id=cur.fetchone()[0]
	cur.execute(''' INSERT OR REPLACE INTO Track(title,album_id,len,count,rating,genre_id) VALUES(?,?,?,?,?,?)''',(name,album_id,length,count,rating,genre_id))
	c.commit()
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
               FROM Track JOIN Genre JOIN Album JOIN Artist 
               ON Track.genre_id = Genre.id and Track.album_id = Album.id 
               AND Album.artist_id = Artist.id
               ORDER BY Artist.name LIMIT 3''')
c.commit()


	
    
