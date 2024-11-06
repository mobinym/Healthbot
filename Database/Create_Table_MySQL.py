import mysql.connector
from mysql.connector import errorcode

# Configuration
config = {
    'user': 'root',
    'password': 'Mobin_ym11228',
    'host': 'localhost', 
    'database': 'Darvishi_db',
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE MedicalJobs (
        JobID INT PRIMARY KEY AUTO_INCREMENT,
        JobTitle VARCHAR(100),
        Department VARCHAR(100),
        RequiredSpecialization VARCHAR(100),
        ExperienceLevel VARCHAR(50),
        Location VARCHAR(100),
        JobType VARCHAR(50),
        SalaryRange VARCHAR(50),
        Description TEXT,
        Requirements TEXT,
        PostingDate DATETIME,
        ApplicationDeadline DATETIME,
        ContactEmail VARCHAR(100),
        ContactPhone VARCHAR(20)
    )
    '''
    
    cursor.execute(create_table_query)
    print("Table 'MedicalJobs' created successfully")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)
finally:
    cursor.close()
    conn.close()
