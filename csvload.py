from mongoengine import *

class coincaps(Document):
    id = IntField()
    data = IntField()
    FactorConfigId = IntField()
    createdAt = DateTimeField()
