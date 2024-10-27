from datetime import datetime,timedelta

class DateHeler:
  @staticmethod
  def expired_time(minutes=60):
    exp=datetime.utcnow() + timedelta(minutes=minutes)
    return exp
