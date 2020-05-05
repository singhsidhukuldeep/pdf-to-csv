# creates connection with the SQL database

import mysql.connector
import params

# returns SQL connection
def getConnection():
    try:
        mydb = mysql.connector.connect(
          host=params.host,
          user=params.username,
          passwd=params.password,
          database=params.db_name
        )
        return mydb
    except Exception as exp:
        print('connection to MySQL DB failed')
        print(exp)
        return None,exp
