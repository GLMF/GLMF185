import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from GmailMessage import GmailMessage


class Gmail:
    def __init__(self, flags, client_secret_file='client_secret.json',
            oauth_scope='https://www.googleapis.com/auth/gmail.readonly',
            storage_file='gmail.storage'):
        self.__client_secret_file = client_secret_file
        self.__oauth_scope = oauth_scope
        self.__storage = Storage(storage_file)
        self.gmail_service = None
        self.__connect(flags)


    def __connect(self, flags):
        flow = flow_from_clientsecrets(self.__client_secret_file, scope=self.__oauth_scope)
        http = httplib2.Http()

        credentials = self.__storage.get()
        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, self.__storage, flags, http=http)

        http = credentials.authorize(http)

        self.gmail_service = build('gmail', 'v1', http=http)


    def getMessagesList(self, userId='me', query=None):
        return self.gmail_service.users().messages().list(userId=userId, q=query).execute()

    def getMessageDetails(self, msgId, userId='me'):
        return GmailMessage(self.gmail_service.users().messages().get(userId=userId, id=msgId).execute())

    def markAsRead(self, msgId, userId='me'):
        self.gmail_service.users().messages().modify(userId=userId, id=msgId, body={'removeLabelIds':['UNREAD'], 'addLabelIds':[]}).execute()
