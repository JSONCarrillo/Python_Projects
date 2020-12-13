#imports sqlite3 module
import sqlite3

#saves connection to database as a variable
conn = sqlite3.connect('assignment1.db')

#creates connection to database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment1.db')

#provided file list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.png')

for items in fileList:
    if items.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_files (col_file) VALUES (?)', (items, ))
            print(items)
conn.close()
