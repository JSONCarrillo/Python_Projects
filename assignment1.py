#imports sqlite3 module
import sqlite3

#saves connection to database as a variable
conn = sqlite3.connect('assignment1.db')

#creates connection to database
with conn:
    #saves function to update database as avariable
    cur = conn.cursor()
    #creates table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    #commits table
    conn.commit()
#closes out of database
conn.close()

#re-calls database
conn = sqlite3.connect('assignment1.db')

#provided file list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.png')

#for loop to iterate through tuple
for items in fileList:
    #if statement that chooses files ending in .txt
    if items.endswith('.txt'):
        #establishes connection to database
        with conn:
            #enables editing in database
            cur = conn.cursor()
            #inserts into table the values matching within the if statement parameter
            cur.execute('INSERT INTO tbl_files (col_file) VALUES (?)', (items, ))
            #prints those items into the console
            print(items)
#closes connection
conn.close()
