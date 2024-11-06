import mysql.connector

# Connection details
host = 'localhost'
database = 'Darvishi_db'
user = 'root' 
password = 'Mobin_ym11228'  


try:
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()


    def get_job_ids_by_title(job_title):
        query = "SELECT JobID FROM MedicalJobs WHERE JobTitle = %s"
        cursor.execute(query, (job_title,))
        job_ids = cursor.fetchall()
        return job_ids

    user_input = input("Enter the Job Title you want to search for: ")
    job_ids = get_job_ids_by_title(user_input)
    
    if job_ids:
        print(f"Job IDs for '{user_input}':")
        for job_id in job_ids:
            print(job_id)
    else:
        print(f"No jobs found for '{user_input}'.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
