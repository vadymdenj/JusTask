# pip install pymysql

import pymysql

host = 'mysql-db.cdql6ypincjq.us-east-1.rds.amazonaws.com'
port = 3306
user = 'admin'
password = 'password'
database = 'turbotask_db'

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

def add_event(uid, event_name, event_address, flexible, start, end, dur):
    # Create a cursor object
    cursor = connection.cursor()
    # Execute a SQL query
    cursor.execute('INSERT INTO scheduler VALUES (%s, %s, %s, %s, %s, %s, %s)', (uid, event_name, event_address, flexible, start, end, dur))
    connection.commit()
    cursor.close()
    connection.close()