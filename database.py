import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='raspberry.rochester.k12.mn.us',
                             user='Mayo4',
                             password='ITLaunch',
                             db='Mayo4',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Products
        sql = "SELECT * from Products"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
