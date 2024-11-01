from project.module.ormsqlachemy import Orm
from .abstraction import AbstractionDataAccess
from project.model.match import Match


class OrmSqlalchemy(AbstractionDataAccess,Orm):
    def create_match(self,duration,location):
        match=Match(duration=duration
                    ,location=location)
        self.add_and_flush(match)
        return match

    def get_match(self,match_id):
        get_match=Match.query.filter(Match.id==match_id,Match.is_deleted==False)
        return get_match
    def update_match(self,match_id,duration):
        updated_match=Match.query.filter(Match.id==match_id,Match.is_deleted==False).first()
        if updated_match:
            updated_match.duration=duration
        return updated_match
    def delete_match(self,match_id):
        deleted_match=Match.query.filter(Match.id==match_id).first()
        if deleted_match:
            deleted_match.is_deleted = True

        return deleted_match
    def search_match(self, duration, location):
   
     match = Match.query.filter(Match.is_deleted == False)

    
     if duration:
        match = match.filter(Match.duration.ilike(f"%{duration}%"))
     if location:
        match = match.filter(Match.location.ilike(f"%{location}%"))

    
     search_results = match.all()

   
     search_data = [{
        "duration": match.duration,
        "location": match.location
     } for match in search_results]

     return search_data
