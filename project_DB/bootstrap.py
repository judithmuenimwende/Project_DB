from models.user import User
from models.invoice import Invoice
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("invoice.db")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Invoice], safe=True)
    try:
      






    except IntegrityError:
        pass
    DATABASE.close()