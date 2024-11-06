import mysql.connector
from mysql.connector import Error


host = 'localhost'  
user = 'root'
password = 'Mobin_ym11228'  

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    
    if conn.is_connected():
        cursor = conn.cursor()
        database_name = "Darvishi_db"
        
        
        create_db_query = f"CREATE DATABASE {database_name}"
        
        
        cursor.execute(create_db_query)
        print(f"Database '{database_name}' created successfully.")
        
except Error as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if conn.is_connected():
        conn.close()
