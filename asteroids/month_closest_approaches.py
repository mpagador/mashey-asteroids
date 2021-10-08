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

    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    intervals = time_intervals(start, end, 7)
    new_data = {'start_date': start_date, 'element_count': 0, 'near_earth_objects': {}}

    for interval in intervals:
        original_data = neo_feed(str(interval[0]), str(interval[1]))
        new_data['element_count'] = new_data['element_count'] + original_data['element_count']
        for key, value in original_data['near_earth_objects'].items():
            new_data['near_earth_objects'][key] = value
    return json.dumps(new_data)

def time_intervals(start, end, interval):
    intervals = []
    while start < end:
        curr = start
        start = start + timedelta(days=interval)
        if start > end:
            intervals.append([curr, end])
        else:
            intervals.append([curr, start])
    return intervals
