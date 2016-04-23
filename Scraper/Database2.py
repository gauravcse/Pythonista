import sqlite3 as sq
import json

conn=sq.connect('roster.sqlite')
cur=conn.cursor()

cur.executescript('''CREATE TABLE IF NOT EXISTS User(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT UNIQUE
                    );
                    CREATE TABLE IF NOT EXISTS Course(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        title TEXT UNIQUE
                    );
                    CREATE TABLE IF NOT EXISTS Member(
                        user_id INTEGER,
                        course_id INTEGER,
                        role INTEGER,
                        PRIMARY KEY(user_id,course_id)
                    );  ''')
fh=open('roster_data.json').read()
j=json.loads(fh)

for line in j :
    name=line[0]
    title=line[1]
    role=line[2]
    print name,title
    cur.execute('''INSERT OR IGNORE INTO User(name) VALUES(?)''',(name,))
    cur.execute('''SELECT id FROM User WHERE name=?''',(name,))
    user_id=cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES(?)''',(title,))
    cur.execute('''SELECT id FROM Course WHERE title=?''',(title,))
    course_id=cur.fetchone()[0]
    cur.execute('''INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES(?,?,?)''',(user_id,course_id,role))
conn.commit()
    
