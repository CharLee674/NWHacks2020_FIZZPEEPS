from datetime import datetime 

class EntrySentiment:
    """Class to represent a journal entry sentiment on a given current time"""
    
    def __init__(self, id):
        """Name is the name of the person, entries represent the entries they have"""
        self.entries = {}
        self.id = id
    
    def insertEntryNow(self, sentiment):
        """Enters the sentiment at the current system datetime"""
        now = datetime.datetime.now()
        self.entries[now] = sentiment

    def insertEntryTime(self, datetime, sentiment):
        """Receives a datetime and sentiment and saves it accordingly"""
        self.entries[datetime] = sentiment

    def deleteEntry(self, date):
        """Deletes the entry at the given datetime"""
        del self.entries[date]

    def getSentiment(self, datetime):
        """Returns the entry at the given datetime and returns a message of 'No log exists at this given time' if not inside"""
        return self.entries.get(datetime, "No log exists at this given time")



a = EntrySentiment("C")
date1 = datetime.now()
sentiment1 = 0.75
a.insertEntryTime(date1, sentiment1)
print(a.getSentiment(date1))

    

