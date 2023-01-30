import datetime

import peewee
from peewee import *

db = MySQLDatabase("editestdb", host="myos", user="editest", passwd="test1234")
db.connect()


class Price(peewee.Model):
    timestamp = peewee.DateField(default=datetime.date.today)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(BTCUSD="11234.56")
    price.save()


if __name__ == "__main__":
    Price.drop_table()
    test_peewee()
