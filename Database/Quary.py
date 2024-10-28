import pyodbc

server = 'MYM-DESKTOP'
database = 'Darvishi_db'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def get_job_ids_by_title(job_title):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    try:
        query = "SELECT JobID FROM MedicalJobs WHERE JobTitle = ?"
        cursor.execute(query, (job_title,))
        
        results = cursor.fetchall()
        job_ids = [result[0] for result in results] 
        return job_ids  

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

user_input = input("Enter the Job Title you want to search for: ")
job_ids = get_job_ids_by_title(user_input)

if job_ids:
    print(f"The Job IDs for '{user_input}' are: {job_ids}")
else:
    print(f"No jobs found with the title '{user_input}'.")
