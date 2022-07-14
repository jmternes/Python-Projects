import sqlite3

conn = sqlite3.connect('test2.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_database( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT)")
    conn.commit()

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_database (col_files) VALUES (?)", \
                        (x,))
            print(x)

conn.close()
