import pymongo
import redis
import mongoengine
from mongoengine import (
    connect,
    DynamicDocument, ObjectIdField,
    StringField, DateTimeField, IntField
)

DATABASE_NAME = "short_chain_application"
connect(DATABASE_NAME, alias=DATABASE_NAME)


class ShortUrl(DynamicDocument):
    id = ObjectIdField(required=True, primary_key=True)
    short_tag = StringField(required=True, max_length=20)
    short_url = StringField(required=True, max_length=20)
    long_url = StringField(required=True)
    visits_count = IntField(required=True)
    created_at = DateTimeField(required=True)
    created_by = StringField(required=True, max_length=20)
    msg_context = StringField(required=True)

    meta = {
        "collection": "c_short_url",
        "db_alias": DATABASE_NAME
    }

    objects: mongoengine.QuerySet


class User(DynamicDocument):
    id = ObjectIdField(required=True, primary_key=True)
    username = StringField(required=True, max_length=20)
    password = StringField(required=True, max_length=32)
    created_at = DateTimeField(required=True)

    meta = {
        "collection": "c_user",
        "db_alias": DATABASE_NAME
    }

    objects: mongoengine.QuerySet


if __name__ == '__main__':
    pass
