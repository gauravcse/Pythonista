import sqlite3

conn=sqlite3.connect('email.sqlite')
cur=conn.cursor()
cur.execute('''CREATE TABLE Counts(org TEXT,count INTEGER)''')
fh=open("C:\Users\Gaurav Mitra\Desktop\Learning\Coursera\code\mbox.txt")
for line in fh :
    if not line.startswith("From: ") :
        continue
    else :
        pieces=line.split()
        email=pieces[1]
        cur.execute('SELECT count FROM Counts WHERE org= ? ',(email,))
        try:
            count=cur.fetchone()[0]
            cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(email,))
        except :
            cur.execute('''INSERT INTO Counts(org,count) VALUES(?,1)''',(email,))
conn.commit()
for row in cur.execute('''SELECT * FROM Counts''') :
    print '{}   {}'.format(str(row[0]),row[1])
cur.close()
