from peewee import (Model, CharField, SqliteDatabase, IntegrityError, DateTimeField,)
import datetime
DATABASE = SqliteDatabase("startech.db")


class Device(Model):
    name = CharField(max_length=100, unique=True)
    dev_id = CharField(max_length=100, unique=True)

    class Meta:
        database = DATABASE


class DeviceLocation(Model):
    lat = CharField(max_length=100)
    long = CharField(max_length=100)
    alt = CharField(max_length=100)
    dev_id = CharField(max_length=100)
    time_ping = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


DATABASE.create_tables([Device, DeviceLocation], safe=True)