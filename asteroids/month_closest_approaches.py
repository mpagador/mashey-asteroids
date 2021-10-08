import json
from .NeoWs import neo_feed

# date format: YEAR-MONTH-DAY
# endpoint can only return 7 days at a time
def month_closest_approaches(start_date):
    