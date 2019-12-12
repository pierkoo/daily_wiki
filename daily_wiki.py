<<<<<<< HEAD
import requests
import database_management as dbm
import urllib.parse
import yagmail
from datetime import datetime

def get_article():
    ''' Gets random article from www.wikipedia.pl. Returns title and link to the article '''


    page=requests.get('https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona')

    # with open('log.txt', 'w', encoding="utf-8") as open_file:
    #     open_file.write(r.text)

    title=urllib.parse.unquote(page.url.split('/')[-1]).replace('_',' ')
    article=[title,page.url]

    return article

def generate_message(article,filename):
    with open('message_template.html', 'r') as original_file:
        original_text=original_file.read()


    modified_text=original_text.replace('ARTICLE_TITLE',article[0])
    modified_text=modified_text.replace('ARTICLE_LINK',article[1])


    with open(filename,'w+',encoding='utf-8') as file:

        file.write(modified_text)


def send_email(message_filename,emails):

    try:
        with yagmail.SMTP({'dailyw.test@gmail.com':'Daily Wiki'}) as yag:
            today=str(datetime.now())
            yag.send(
            bcc=emails,
            subject='DailyW for '+today,
            contents=message_filename
            )
        print("Emails have been sent!")
        return True
    except:
        print("Emails were not sent!")
        return False


database = r"daily_wiki_database.db"
filename='message.html'


with dbm.create_connection(database) as conn:

    while True:
        article=get_article()
        try:
            dbm.add_article(conn,article)
            break
        except dbm.sqlite3.IntegrityError:
            print('Article already in the database!')

    # for line in dbm.show_all_articles(conn):
    #     print(line)

    subs=dbm.show_all_subscribers(conn)

generate_message(article,filename)

emails=[element[1] for element in subs]

send_email(filename,emails)


=======
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

>>>>>>> 59797801e30683431b5e9e30605ff83020776041
