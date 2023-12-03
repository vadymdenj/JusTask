# pip install mysql-connector-python

import mysql.connector

endpoint = 'mysql-db.cdql6ypincjq.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'password'
database = 'turbotask_db'

cnx = mysql.connector.connect(user=username, password=password,
                              host=endpoint, database=database)

cursor = cnx.cursor()

create_table_query = '''
CREATE TABLE scheduler (
  uid VARCHAR(64) NOT NULL UNIQUE,
  type VARCHAR(1) NOT NULL,
  task_address VARCHAR(128) NOT NULL,
  start INT, 
  end INT,
  dur INT
)
'''

cursor.execute(create_table_query)

# commit the changes
cnx.commit()

# close cursor and connection objects
cursor.close()
cnx.close()



