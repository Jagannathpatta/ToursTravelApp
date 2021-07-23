import cx_Oracle
import os
# os.environ["LD_LIBRARY_PATH"] = "/home/jagannath/jaggu/instantclient_21_1"
# conn = cx_Oracle.connect('http://hoteldb.cszedp6qqa8n.ap-south-1.rds.amazonaws.com:1521/HOTELDB')

# TNS_ADMIN=C:\Users\KALPESH\Oracle\network\admin;USER ID=ADMIN;DATA SOURCE=hoteldb.cszedp6qqa8n.ap-south-1.rds.amazonaws.com:1521/HOTELDB:1521

# conn = cx_Oracle.connect('hoteldb.cszedp6qqa8n.ap-south-1.rds.amazonaws.com:1521/HOTELDB')

# connection = cx_Oracle.connect(user="admin", password="admin1234",
#                                dsn="hoteldb.cszedp6qqa8n.ap-south-1.rds.amazonaws.com:1521/HOTELDB",
#                                encoding="UTF-8")

# connection = cx_Oracle.connect(user="admin", password="travel123",
#                                dsn="traveldbinstance.cuufmgkyv6ao.ap-south-1.rds.amazonaws.com:1521/TRAVELDB",
#                                encoding="UTF-8")

connection = cx_Oracle.connect(user="admin", password="travel123",
                               dsn="tourtraveldb.cuufmgkyv6ao.ap-south-1.rds.amazonaws.com:1521/TRAVELDB",
                               encoding="UTF-8")
cursor = connection.cursor()
cursor.execute(" insert into train (TRAIN_NO , TRAIN_NAME , COST_PER_SEAT , SOURCE_STATE , SOURCE_DISTRICT , SOURCE_CITY , SOURCE_PINCODE , SOURCE_LINE , DESTN_STATE , DESTN_DISTRICT , DESTN_CITY , DESTN_PINCODE , DESTN_LINE , DEPARTURE_DATE , DEPARTURE_TIME , ARRIVAL_DATE , ARRIVAL_TIME , ADMIN_ID ) values('20110' , 'XSS Express' , 870 , 'Maha' , 'Mum' , 'Mum' , 400612 , '307/Apt.' , 'Odisha' , 'Ganjam' , 'Brahmapur' , 760011 , 'B Street' , '14-Mar-2021' , '10:00' , '16-Mar-2021' , '22:00' , 21 ) ")
connection.commit()
# cursor.execute("SELECT * FROM UserDetails ")
# for row in cursor:
#     print(row)
print(connection.version)
cursor.close()
connection.close()