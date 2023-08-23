#SQL : It is Structured Query Language##
#DDL: Create, Alter, Drop, Truncate.
#DML: Insert, Update, Delete.
#DRL: Select
#TCL: Commit, Rollback
#DCL: Grant, Revoke

#We preform the query Insert, Update, Delete

import mysql.connector


insert_query = "insert into student values(104,'Kim')"
update_query = "update student set snmae = 'Mary' where sid=104;"
delete_query = "delete from student where sid=104"

try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
    curs=con.cursor()  #Here we are creating cursor
    #curs.execute("insert into student values( 104,'Kim')") # Here we are executing query through cursor.
    curs.execute("select * from orders")
    for row in curs:
        print(row[0],row[1],row[2])    # this will print the output which select command fetch.

    #con.commit()  # commit the transaction


    con.close()

except:
    print("Connection is unsuccessful")

print("Finished the insertion")

