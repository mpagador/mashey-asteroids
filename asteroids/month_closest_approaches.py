import json, calendar
from datetime import datetime, date, timedelta
from .neows import neo_feed

# date format: YEAR-MONTH-DAY, xxxx-xx-xx
# endpoint can only return 7 days at a time
def month_closest_approaches(start_date):
    year = start_date[:4]
    month = start_date[5:7]
    last_day = calendar.monthrange(int(year), int(month))[1]
    end_date = year + '-' + month + '-' + str(last_day)
    intervals = time_intervals(date(start_date), date(end_date), 7)
    new_data = {'start_date': start_date, 'element_count': 0, 'near_earth_objects': {}}

    for interval in intervals:
        original_data = neo_feed(str(interval[0]), str(interval[1]))
        


def time_intervals(start, end, interval):
    intervals = []
    while start < end:
        curr = start
        start = start + timedelta(days=interval)
        intervals.append([curr, start])
    intervals.append([start, end])
    return intervals
