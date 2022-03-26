import sqlite3

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("database.db")

c = conn.cursor()

# c.execute('CREATE TABLE books (title TEXT, pages INTEGER)')
# no error for multiple time run-----
# c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
# multiline query need to use '''-------
c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')


# insert only one column value (title only)---------
# c.execute('INSERT INTO books(title) VALUES ("Learn Python")')
# c.execute('INSERT INTO books VALUES ("Learn python", 72)')
# conn.commit()

# c.execute('SELECT * FROM books')
# #fetchall() fro all data from table
# data = c.fetchone()

# books = [
#     ("Learn OOP", 80),
#     ("Design Pettern", 101),
#     ("Learn NodeJS", 200)
# ]

# c.executemany ('INSERT INTO books VALUES (?, ?)',books)
# conn.commit()

# c.execute('SELECT * FROM books WHERE title="Learn OOP"')
c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)

# c.execute('DELETE FROM books WHERE title ="Learn OOP"')
# single '=' for compare value in sql!(rowid=17)-------
# c.execute('DELETE FROM books WHERE rowid=17')
# conn.commit()

#update data (this is not ideal way to update with hardcoded id, need to create a function, that will update (call SDK)----------------
c.execute('UPDATE books SET title ="New Programming book OOP" WHERE rowid=1')

update_book(book,)


#SDK-----------


# select table column and data------------
c.execute('SELECT rowid, title FROM books')
data = c.fetchall()
print(data)





