import mongoengine, lagou_config

mongoengine.connect(db=lagou_config.DATABASE, host=lagou_config.HOST, port=lagou_config.PORT)
class Lagou_Position(mongoengine.Document):
    positionId = mongoengine.StringField()
    positionName = mongoengine.StringField()
    companyId = mongoengine.StringField()
    companyFullName = mongoengine.StringField()
    city = mongoengine.StringField()
    district = mongoengine.StringField()
    jobNature = mongoengine.StringField()
    industryField = mongoengine.StringField()
    salary = mongoengine.StringField()
