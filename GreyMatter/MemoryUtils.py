import sqlite3
import datetime

# TLDR Style Notes
# From linux prompt: > sqlite3
# cd to directory and create database:
#> Sqlite3 masterbrain.db
#> This gives Sqlite3 prompt
#sqlite> .open masterbrain.db
#sqlite> .help
#sqlite> .quit
# sqlite>  drop database
# sqlite>  create database



def dropTable():
    conn = sqlite3.connect("masterbrain.db")
    c = conn.cursor()
    c.execute("DROP TABLE test")
    conn.commit()
    conn.close()

def createTable():
    conn = sqlite3.connect("masterbrain.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE test (category text, thought text, whenInserted datetime)"""
    )
    conn.commit()
    conn.close()


def saveToDatabase(type, thought):

    conn = sqlite3.connect("masterbrain.db")
    # conn.SetPassword("test")
    now = datetime.datetime.now()
    c = conn.cursor()
    c.execute(
        "insert into test (category, thought, whenInserted) values (?, ?, ?)",
        (type, thought, now),
    )

    conn.commit()
    conn.close()


# saveToDatabase("test2", "test2", now)

# function to retrieve from database
def retrieveFromDatabase(type):
    # conn = sqlite3.connect("masterbrain.db", Password="test")
    conn = sqlite3.connect("masterbrain.db")
    c = conn.cursor()
    # c.execute("""SELECT * FROM players WHERE team = ?;"""), (team_name,))
    # results = c.fetchall()
    c.execute("SELECT * FROM test WHERE category = ?;", (type,))
    result = c.fetchall()
    print("done")
    print(result)
    conn.close()

# dropTable()
# createTable()
# saveToDatabase("test1", "test1")
# saveToDatabase("test2", "test2")
# saveToDatabase("test3", "test3")
retrieveFromDatabase("test3")

