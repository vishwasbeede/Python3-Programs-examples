import mysql.connector
from mysql.connector import errorcode
import datetime


# host=input("Enter host name:\n")
# users=input("Enter user name:\n")
# password=input("Enter paswword name:\n")
# database=input("Enter database name:\n")


# config = {
  # 'user': 'scott',
  # 'password': 'password',
  # 'host': '127.0.0.1',
  # 'database': 'employees',
  # 'raise_on_warnings': True
# }

# cnx = mysql.connector.connect(**config)

# cnx.close()



#host=input("Enter host name:\n"),users=input("Enter user name:\n"),password=input("Enter paswword name:\n"),database=input("Enter database name:\n")


  # host="localhost",
  # user="root",
  # password="vishwasbg",
  # database="village"

#a,b,b,c,d=host,users,password,database

#host=input("Enter host name:\n"),users=input("Enter user name:\n"),password=input("Enter paswword name:\n"),database=input("Enter database name:\n")
try:
    mydb_1=mysql.connector.connect(host="localhost",user="root",password="vishwasbg",database="village")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

else:
    #mydb = mysql.connector.connect()
# mydb = mysql.connector.connect()
# print(mydb)
    #print(mydb_1)
    cursor=mydb_1.cursor()
    #cursor.execute("SHOW DATABASES")
    #cursor.execute("USE 'backup_new'")
    #cursor.execute("SHOW TABLES")
    cursor.execute("SELECT home_id,home_name,members_no from home_table;")
    
    #cursor.execute("SHOW COLUMNS FROM home_table;")
    
    
    # query = ("SELECT first_name, last_name, hire_date FROM employees "
         # "WHERE hire_date BETWEEN %s AND %s")

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)
    
    
    
    
# mydb.close()
    #print (type(cursor))
    for (home_id,home_name,members_no) in cursor:
        print("{} home identity number is given as {} on".format(home_name,home_id))
        print(datetime.datetime.now().date())
        print("\n")
        
    mydb_1.close()
# mydb.execute("SHOW DATABASES")


# for (first_name, last_name, hire_date) in cursor:
  # print("{}, {} was hired on {:%d %b %Y}".format(
    # last_name, first_name, hire_date))



# for x in my_cursor:
    # print(x)
    
    

# mydb.close()