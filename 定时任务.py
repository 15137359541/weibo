from datetime import datetime,timedelta
SECONDS_PER_DAY = 24 *60 * 60
def doFirst():
    curTime=datetime.now()
    print curTime
    desTime = curTime.replace(hour=2,minute=0,second=0,microsecond=0)
    print desTime
    delta = curTime - desTime
    print delta
    skipSeconds =SECONDS_PER_DAY -delta.total_seconds()
    print skipSeconds
doFirst()