import requests
import database_management as dbm
import urllib.parse


r=requests.get('https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona')



# with open('log.txt', 'w', encoding="utf-8") as open_file:
#     open_file.write(r.text)

    title=urllib.parse.unquote(r.url.split('/')[-1]).replace('_',' ')
    article=[title,r.url]

    database = r"daily_wiki_database.db"

    with dbm.create_connection(database) as comm:

        try:
            dbm.add_article(comm,article)
        except dbm.sqlite3.IntegrityError:
            print('Article already in the database!')

        dbm.show_all_articles(comm)

