# -*- coding:utf-8 -*-
import argparse
import re
import sqlite3
from oauth2client.tools import argparser
from Gmail import Gmail

if __name__ == '__main__':
    parser = argparse.ArgumentParser(parents=[argparser])
    flags = parser.parse_args()

    # Ouverture de la base de données
    try:
        print 'Ouverture de la base <links.db>'
        base = sqlite3.connect('links.db')
        cursor = base.cursor()
        cursor.execute('create table links (id integer primary key, tag text, url text);')
        base.commit()
        print 'Table <links> créée !'
    except sqlite3.OperationalError:
        print 'Table <links> trouvée !'

    gmail = Gmail(flags, oauth_scope='https://www.googleapis.com/auth/gmail.modify')
    messages = gmail.getMessagesList(query='is: unread')
    pattern = re.compile(r'^\[#(\w+)\]')

    if messages['messages']:
        for msg in messages['messages']:
            m = gmail.getMessageDetails(msg['id'])
            if m.getFrom().startswith('Tristan Colombo'):
                subject = m.getSubject()
                tag = pattern.search(subject)
                if tag is not None:
                    link = m.getSnippet()
                    print 'Ajout du lien {} avec le tag {}'.format(link, tag.group(1))
                    cursor.execute('insert into links(tag, url) values("{}", "{}");'.format(tag.group(1), link))
                    base.commit()
                    gmail.markAsRead(msg['id'])


    print 'Mails lus : {}'.format(len(messages['messages']))

    rows = cursor.execute('select * from links')
    for data in rows:
        print '[{}] {} : {}'.format(data[0], data[1], data[2])

    # Fermeture de la base de données
    cursor.close()
    base.close()
