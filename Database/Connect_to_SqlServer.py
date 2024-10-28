import pyodbc

server = 'MYM-DESKTOP'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};Trusted_Connection=yes;'

conn = pyodbc.connect(connection_string, autocommit=True)
cursor = conn.cursor()

database_name = "YourDatabaseName"
create_db_query = f"CREATE DATABASE {database_name}"

try:
    cursor.execute(create_db_query)
    print(f"Database '{database_name}' created successfully.")
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
