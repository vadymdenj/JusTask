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
cursor.execute('SELECT * FROM scheduler')

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
connection.close()