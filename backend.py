import sqlite3

def connect():
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn_obj.commit()
    conn_obj.close()

def insert(title, author, year, isbn):
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn_obj.commit()
    conn_obj.close()

def view():
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * FROM book")
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows

def update(id, title, author, year, isbn):
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn_obj.commit()
    conn_obj.close()

def delete(id):
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("DELETE FROM book WHERE id = ?", (id,))
    conn_obj.commit()
    conn_obj.close()

def search(title = "", author = "", year = "", isbn = ""):
    conn_obj = sqlite3.connect("books.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows
    
connect()