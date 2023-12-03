import sys
from app.utils.utils import getTravelTime
from app.utils.auth_utils import get_token

from datetime import datetime, timezone, timedelta

from location_conv import addr_to_loc
# Get the current date and time
now = datetime.now(timezone.utc)

# Convert to ISO 8601 format
iso_format = now.isoformat()

task = {"name":"Grocery Shopping","duration":30, "address":"2901 Pacific Ave San Francisco, CA 94115"}

wake = {"name":"sleep",
        "start":"2300",
        "end":"0700",
        "address":"943 S Van Ness Ave San Francisco, CA 94110"}
event1 = {"name":"CSE 373",
          "start":"1430",
          "end":"1520",
          "address":"1299 18th St San Francisco, CA 94107"}
event2 = {"name":"CSE 311",
          "start":"1630",
          "end":"1720",
          "address":"450 10th St, San Francisco, CA 94103"}
event3 = {"name":"gym",
          "start":"1930",
          "end":"2130",
          "address":"840 Brannan St San Francisco, CA 94103"}
calendar = [wake,event1,event2,event3]
interval = 15
def fastest_travel(task, calendar):
    try:
        fastest_travel = sys.maxsize
        slowest_travel = 0
        returned = ""
        for i in calendar:
            j = next(calendar,i)
            if j != -1:
                s_t = convert(j.get("start"), now)
                e_t = convert(i.get("end"), now)
                s_a = i.get("address")
                e_a = j.get("address")
                dur = timedelta(minutes=task.get("duration"))
                new_time = e_t + timedelta(minutes=k*interval)
                if duration(s_t, e_t) >= dur:
                    # statement = getTravelTime(get_token(), '37.770637, -122.412435', '37.781613, -122.494546', e_t)
                    statement = getTravelTime(get_token(), addr_to_loc(s_a), addr_to_loc(task.get("address")), new_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
                    print("statement",statement)
                    if fastest_travel > int(statement):
                        fastest_travel = int(statement)
                        returned = new_time.strftime("%H%M")
                    if slowest_travel < int(statement):
                        slowest_travel = int(statement)
        return f"Fastest Travel Time: {fastest_travel}mins, You saved: {slowest_travel-fastest_travel} minutes ,Task Start Time: {returned}"
        
    except:
        return -1
# def fastest_travel(task, calendar):
#     fastest_travel = sys.maxsize
#     returned = -1
#     for i in calendar:
#         j = next(calendar,i)
#         if j != -1:
#             s_t = j.get("start")
#             e_t = i.get("end")
#             s_a = i.get("address")
#             e_a = j.get("address")
#             dur = task.get("duration")
#             for k in range(int(dur/interval)):
#                 e_t = str(int(e_t)+k*interval)
#             if duration(s_t, e_t) >= dur:
#                 # statement = getTravelTime(get_token(), s_a, e_a, now.replace(hour=e_t[0:1], minute=e_t[2:3],second=0,millisecond=0))
#                 statement = getTravelTime(get_token(), '37.770637, -122.412435', '37.781613, -122.494546', '2023-12-09T10:42:41Z')

#                 if fastest_travel > statement:
#                     fastest_travel = statement
#     return e_t

# getTravelTime(token, '37.770637, -122.412435', '37.781613, -122.494546', '2023-12-09T10:42:41Z')


def convert(time, now):
    return now.replace(hour=int(time[0:2]),minute=int(time[2:4]),second=0,microsecond=0)
def next(list,index):
    i = list.index(index)
    if i+1 >= len(list):
        return -1
    return list[i+1]
def duration(start, end):
    return start-end

# def main():
    
#     print('\n',fastest_travel(task, calendar))

# main()

