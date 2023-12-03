# pip install pymysql

import pymysql

host = 'tasks-db.cdql6ypincjq.us-east-1.rds.amazonaws.com'
port = 3306
user = 'admin'
password = 'password'
database = 'justask_db'

# Connect to the database
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

def get_event(uid):
    # Create a cursor object
    cursor = connection.cursor()
    # Execute a SQL query
    cursor.execute('SELECT * FROM scheduler where uid = %s', (uid))
    # Fetch the results
    results = cursor.fetchall()
    print(results)
    connection.commit()
    cursor.close()
    connection.close()
    returned = []
    for i in results:
        returned.append= ({"uid":i[0],
                "event_name":i[1],
                "address":i[2],
                "flexible":i[3],
                "start":i[4],
                "end":i[5]
        })
    return returned

def add_event(uid, event_name, event_address, flexible, start, end, dur):
    # Create a cursor object
    cursor = connection.cursor()
    # Execute a SQL query
    cursor.execute('INSERT INTO scheduler VALUES (%s, %s, %s, %s, %s, %s, %s)', (uid, event_name, event_address, flexible, start, end, dur))
    connection.commit()
    cursor.close()
    connection.close()

#add_event("santiago", "golfing", "8 Presidio Terrace, San Francisco, CA 94118", "N", "1400", "1500", 60)
#add_event("santiago", "brunch", "401 Geary St, San Francisco, CA 94102", "N", "1000", "1100", 60)
#add_event("santiago", "shopping", "2801 Bryant St, San Francisco, CA 94110", "Y", "null", "null", 60)