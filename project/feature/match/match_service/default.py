from .abstraction import AbstractionService
from ..excption import MatchNotFound
from ..data_classes import MatchDataClass,UpdateMatch
class Default(AbstractionService):
    def __init__(self,data_access):
              self.data_access=data_access

    def create_match(self,duration,location):
           
           match=self.data_access.create_match(duration,location)
           if not match:
                  raise MatchNotFound()
           return MatchDataClass(
                  id=match.id,
                  duration=match.duration,
                  location=match.location,
                  date=match.date
           )
    def get_match(self,match_id):
           get_match=self.data_access.get_match(match_id)
           if not get_match:
                  raise MatchNotFound
           return MatchDataClass(
                  id=get_match.id,
                  duration=get_match.duration,
                  location=get_match.location,
                  date=get_match.date
           )
    def update_match(self,match_id,duration):
           updated_match=self.data_access.update_match(match_id,duration)
           if not updated_match:
                  raise MatchNotFound
           return UpdateMatch(
                  id=updated_match.id,
                  duration=updated_match.duration
           )

    def search_match(self,duration,location):
           search=self.data_access.search_update(duration,location)
           if not search:
                  raise MatchNotFound(duration=duration)
           return MatchDataClass(
                  id=search.id,
                  duration=search.duration,
                  location=search.location,
                  date=search.date
           )
          