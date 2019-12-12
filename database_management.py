<<<<<<< HEAD
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    ''' Create connectiond to a SQLite dataqbase '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print('Successfully connected to database!')
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    ''' Create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE sql statement
    '''

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:

        print(e)

def add_subscriber(conn, email):
    ''' Add new email adress to subscribers table'''

    sql = ''' INSERT INTO subs(email)
              VALUES(?) '''
    c = conn.cursor()
    c.execute(sql,(email,))


def delete_subscriber(conn, email):
    ''' Deletes email from subscribers '''
    sql = ''' DELETE FROM subs WHERE email = ?'''
    c=conn.cursor()
    c.execute(sql, (id,))
    conn.commit()


def add_article(conn, article):
    ''' Add new article to articles table '''
    sql = ''' INSERT INTO articles(title,link)
              VALUES(?,?) '''
    c = conn.cursor()
    c.execute(sql,article)

def show_all_subscribers(conn):
    ''' Prints all subscribers '''

    sql = ' SELECT * FROM subs '

    c= conn.cursor()
    c.execute(sql)
    rows = c.fetchall()

    return rows

def show_all_articles(conn):
    ''' Prints all subscribers '''

    sql = ' SELECT * FROM articles '

    c= conn.cursor()
    c.execute(sql)
    rows = c.fetchall()

    return rows

def start_database():
    database = r"daily_wiki_database.db"

    sql_create_subscribers_table = ''' CREATE TABLE IF NOT EXISTS subs (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       email text NOT NULL UNIQUE,
                                       joined time NOT NULL DEFAULT (CURRENT_TIMESTAMP)
                                       ); '''
    sql_create_articles_table =    ''' CREATE TABLE IF NOT EXISTS articles (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       title text NOT NULL UNIQUE,
                                       link text NOT NULL UNIQUE,
                                       added time NOT NULL DEFAULT (CURRENT_TIMESTAMP)

                                       ); '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_subscribers_table)
        create_table(conn, sql_create_articles_table)

    else:
        print("Error! Cannot connect to the database!")

    # Automatically populating table with starter emails.
    # p='pierkoo+'
    # en='@gmail.com'
    # email=[p+str(e)+en for e in range(10)]

    # for e in email:
    #     with conn:
    #         try:
    #             add_subscriber(conn,e)
    #         except sqlite3.IntegrityError:
    #             print('Email already in the database!')




    show_all_subscribers(conn)
    show_all_articles(conn)


    conn.close()
if __name__ == '__main__':

    start_database()
=======
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    ''' Create connectiond to a SQLite dataqbase '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    ''' Create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE sql statement
    '''

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:

        print(e)

def add_subscriber(conn, email):
    ''' Add new email adress to subscribers table'''

    sql = ''' INSERT INTO subs(email)
              VALUES(?) '''
    c = conn.cursor()
    c.execute(sql,(email,))


def delete_subscriber(conn, email):
    ''' Deletes email from subscribers '''
    sql = ''' DELETE FROM subs WHERE email = ?'''
    c=conn.cursor()
    c.execute(sql, (id,))
    conn.commit()


def add_article(conn, article):
    ''' Add new article to articles table '''
    sql = ''' INSERT INTO articles(title,link)
              VALUES(?,?) '''
    c = conn.cursor()
    c.execute(sql,article)

def show_all_subscribers(conn):
    ''' Prints all subscribers '''

    sql = ' SELECT * FROM subs '

    c= conn.cursor()
    c.execute(sql)
    rows = c.fetchall()

    for row in rows:
        print(row)

def show_all_articles(conn):
    ''' Prints all subscribers '''

    sql = ' SELECT * FROM articles '

    c= conn.cursor()
    c.execute(sql)
    rows = c.fetchall()

    for row in rows:
        print(row)


def start_database():
    database = r"daily_wiki_database.db"

    sql_create_subscribers_table = ''' CREATE TABLE IF NOT EXISTS subs (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       email text NOT NULL UNIQUE,
                                       joined time NOT NULL DEFAULT (CURRENT_TIMESTAMP)
                                       ); '''
    sql_create_articles_table =    ''' CREATE TABLE IF NOT EXISTS articles (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       title text NOT NULL UNIQUE,
                                       link text NOT NULL UNIQUE,
                                       added time NOT NULL DEFAULT (CURRENT_TIMESTAMP)

                                       ); '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_subscribers_table)
        create_table(conn, sql_create_articles_table)

    else:
        print("Error! Cannot connect to the database!")

    # Automatically populating table with starter emails.
    # p='pierkoo+'
    # en='@gmail.com'
    # email=[p+str(e)+en for e in range(10)]

    # for e in email:
    #     with conn:
    #         try:
    #             add_subscriber(conn,e)
    #         except sqlite3.IntegrityError:
    #             print('Email already in the database!')




    show_all_subscribers(conn)
    show_all_articles(conn)


    conn.close()
if __name__ == '__main__':

    start_database()
>>>>>>> 59797801e30683431b5e9e30605ff83020776041
