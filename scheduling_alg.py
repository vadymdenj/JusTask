import sys

task = {"name":"Grocery Shopping","duration":30, "address":"111 ave ne"}

event1 = {"name":"CSE 373",
          "start":1430,
          "end":1520,
          "address":"GUG hall"}
event2 = {"name":"CSE 311",
          "start":1630,
          "end":1720,
          "address":"CSE2"}
event3 = {"name":"gym",
          "start":1930,
          "end":2130,
          "address":"ima"}

calendar = [event1,event2,event3]
interval = 15
def fastest_travel(task, calendar):
    fastest_travel = sys.maxsize
    returned = -1
    for i in calendar:
        j = next(calendar,i)
        if j != -1:
            s_t = j.get("start")
            e_t = i.get("end")
            s_a = i.get("address")
            e_a = j.get("address")
            dur = task.get("duration")
            for k in range(int(dur/interval)):
                e_t += k*interval
            if duration(s_t, e_t) >= dur:
                statement = get_travel(s_a, e_a, e_t)+get_travel(task.get("address"),e_a,e_t+dur+fastest_travel)
                if fastest_travel > statement:
                    fastest_travel = statement
    return e_t

def get_travel(f, t, dt):
    return 15
def next(list,index):
    i = list.index(index)
    if i+1 >= len(list):
        return -1
    return list[i+1]
def duration(start, end):
    hours = int((start-end)/100)
    minutes = (start-end) % 100
    return hours*60 + minutes
def main():
    print('\n'*100,fastest_travel(task, calendar))

main()

