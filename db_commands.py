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

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
#cursor.execute('INSERT INTO scheduler VALUES (%s, %s, %s, %s, %s, %s)', ("santiago", "E", "1410 NE Campus Pkwy Seattle, WA 98195", "1400", "1500", 60))

cursor.execute('SELECT * FROM scheduler')

# Fetch the results
results = cursor.fetchall()

connection.commit()

# Print the results
print(results)

# Close the cursor and connection
cursor.close()
connection.close()