from google.appengine.ext import ndb

class Post(ndb.Expando):
    name = ndb.StringProperty()
    price = ndb.StringProperty()
    date = ndb.DateProperty()
    url = ndb.StringProperty()
    description = ndb.StringProperty()

    def getValue(self):
        return {
            'name': self.name,
            'price': self.price,
            'date': self.date,
            'url': self.url,
            'description': self.description
        }
