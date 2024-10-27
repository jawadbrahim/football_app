from database.postgres import db

class Orm:
    def add(self,obj):
        db.session.add(obj)
    def commit(self):
        db.session.commit()
    def delete(self,obj):
        db.session.delete(obj)
    def add_and_flush(self,obj):
        db.session.add(obj)
        db.session.flush()