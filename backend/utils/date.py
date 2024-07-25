import datetime

# this function is for Tokyo timezone.
def get_current_date():
    tokyo_time = datetime.timezone(datetime.timedelta(hours=9))
    current_date = datetime.datetime.now(tokyo_time)
    
    return current_date