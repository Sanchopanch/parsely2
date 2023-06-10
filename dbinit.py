import sqlite3
from datetime import date

def createDB():
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    sqlite_create_table_query = 'CREATE TABLE IF NOT EXISTS  querries (\
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                  querry TEXT NOT NULL);'

    sqlite_create_table_query2 = 'CREATE TABLE IF NOT EXISTS  serp (\
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                  date TEXT,\
                                  num INTEGER,\
                                  querry INTEGER NOT NULL, \
                                  site TEXT);'
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection = sqlite3.connect('baseSerp.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query2)
    sqlite_connection.commit()
    print("Таблицы SQLite созданы")
    cursor.close()

def insert_serp(querry, serp_list):
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f'SELECT id from querries where querry = "{querry}"'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchone()
    if record == None:
        sql = f'INSERT INTO querries (id, querry)\
              VALUES(?, ?)'
        cursor.execute(sql, (None, querry))
        sqlite_connection.commit()
    cursor.execute(sqlite_select_query)
    record = cursor.fetchone()
    id = record[0]
    today = str(date.today())

    sqlite_select_query = f'SELECT * from serp where querry = {id} and date="{today}"'
    cursor.execute(sqlite_select_query)
    record = cursor.fetchone()
    if not record == None:
        sql = f'DELETE from serp where querry = {id} and date="{today}"'
        cursor.execute(sql)
        sqlite_connection.commit()
        print(f'deleted from {today}')

    for i, site in enumerate(serp_list):
        sql = f'INSERT INTO serp (id, date, num, querry, site)\
              VALUES(?, ?, ?, ?, ?)'
        cursor.execute(sql, (None, today, i+1, id, site))
    sqlite_connection.commit()
    print(f'insterted {i+1} rows')


    cursor.close()
    sqlite_connection.close()

def add_from_csv():
    sqlite_connection = sqlite3.connect('baseSerp.db', timeout=10)
    cursor = sqlite_connection.cursor()
    # sql = f'INSERT INTO querries (id, querry)\
    #       VALUES(?, ?)'
    # cursor.execute(sql, (None, 'kochetkov spb')) #3
    # cursor.execute(sql, (None, 'kochetkov'))     #4
    # sqlite_connection.commit()

    sql = f'INSERT INTO serp (id, date, num, querry, site)\
          VALUES(?, ?, ?, ?, ?)'

    import csv
    with open("kochetkov spb.csv", newline='') as csvfile:
        serp = csv.reader(csvfile)
        for row in serp:
            cursor.execute(sql, (None, row[0], row[1], 3, row[2]))
            sqlite_connection.commit()
            print(row)
    with open("kochetkov.csv", newline='') as csvfile:
        serp = csv.reader(csvfile)
        for row in serp:
            cursor.execute(sql, (None, row[0], row[1], 4, row[2]))
            sqlite_connection.commit()
            print(row)

    cursor.close()
    sqlite_connection.close()



if __name__ == '__main__':
    createDB()
    # add_from_csv()
    # insert_serp('test', ['site1', 'site2'])
    # insert_serp('test 2', ['site3', 'site4'])
