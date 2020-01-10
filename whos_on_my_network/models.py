import datetime

import peewee

from . import config


database = peewee.SqliteDatabase(
    config.DATABASE_SQLITE_FILE_LOCATION,
    pragmas={
        'foreign_keys': 1  # Enforce foreign-key constraints
    }
)


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Scan(BaseModel):
    """ Scans done on a network """
    id = peewee.PrimaryKeyField(constraints=[peewee.SQL('AUTOINCREMENT')])
    scan_time = peewee.DateTimeField(default=datetime.datetime.now)
    network_id = peewee.TextField()


class Discovery(BaseModel):
    """ A discovered device """
    id = peewee.PrimaryKeyField(constraints=[peewee.SQL('AUTOINCREMENT')])
    scan = peewee.ForeignKeyField(Scan)
    mac_address = peewee.TextField()
    ip_address = peewee.TextField()
    hostname = peewee.TextField(null=True)


database.connect()
database.create_tables([Scan, Discovery])
