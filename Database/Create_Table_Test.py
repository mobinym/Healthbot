import pyodbc


server = 'MYM-DESKTOP'
database = 'Darvishi_db'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'


conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Create the table
create_table_query = '''
CREATE TABLE MedicalJobs (
    JobID INT PRIMARY KEY IDENTITY(1,1),
    JobTitle NVARCHAR(100),
    Department NVARCHAR(100),
    RequiredSpecialization NVARCHAR(100),
    ExperienceLevel NVARCHAR(50),
    Location NVARCHAR(100),
    JobType NVARCHAR(50),
    SalaryRange NVARCHAR(50),
    Description NVARCHAR(MAX),
    Requirements NVARCHAR(MAX),
    PostingDate DATETIME,
    ApplicationDeadline DATETIME,
    ContactEmail NVARCHAR(100),
    ContactPhone NVARCHAR(20)
)
'''
cursor.execute(create_table_query)
conn.commit()


try:
    cursor.execute(create_table_query)
    conn.commit()
    print("create_table_query succssefully")
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
