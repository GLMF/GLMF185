class GmailMessage:
    def __init__(self, data):
        self.__data = { k : v for k, v in zip(map(lambda m: m['name'], data['payload']['headers']), map(lambda m: m['value'], data['payload']['headers'])) }
        self.__data['labels'] = data['labelIds']
        self.__data['snippet'] = data['snippet']

    def getSubject(self):
        return self.__data['Subject'].encode('utf-8')

    def getFrom(self):
        return self.__data['From'].encode('utf-8')

    def getTo(self):
        return self.__data['To'].encode('utf-8')

    def getSnippet(self):
        return self.__data['snippet'].encode('utf-8')

    def isUnread(self):
        return 'UNREAD' in self.__data['labels']
