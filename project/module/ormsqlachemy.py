from database.postgres import db

class Orm:
    def add(self,obj):
        db.session.add(obj)
    def commit(self):
        db.session.commit()
    def delete(self,obj):
        db.session.delete(obj)
    def scalar(self,query):
     return db.session.query(query).scalar()