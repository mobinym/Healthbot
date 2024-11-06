import mysql.connector


conn = mysql.connector.connect(
    host='localhost',          
    user='root',      
    password='Mobin_ym11228',  
    database='Darvishi_db'      
)

cursor = conn.cursor()

insert_data_query = '''
INSERT INTO MedicalJobs (JobTitle, Department, RequiredSpecialization, ExperienceLevel, Location, JobType, SalaryRange, Description, Requirements, PostingDate, ApplicationDeadline, ContactEmail, ContactPhone)
VALUES
('Orthopedics', 'Orthopedics', 'Orthopedic Surgery', 'Senior', 'Los Angeles', 'Full-Time', '$250,000 - $300,000', 'Join our orthopedic team.', 'MD degree, orthopedic residency, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 123-4567'),
('Orthopedics', 'Orthopedics', 'Orthopedic Surgery', 'Mid-Level', 'San Francisco', 'Full-Time', '$200,000 - $250,000', 'Looking for a skilled Orthopedic Surgeon.', 'MD degree, orthopedic residency, 3+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 234-5678'),
('Orthopedics', 'Orthopedics', 'Orthopedic Surgery', 'Entry-Level', 'Miami', 'Part-Time', '$150,000 - $200,000', 'Entry-level Orthopedic position available.', 'MD degree, orthopedic residency.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 345-6789'),
('Dentist', 'Dental', 'Dentistry', 'Senior', 'New York', 'Full-Time', '$150,000 - $200,000', 'Looking for a dedicated Dentist.', 'DDS or DMD, dental license, experience preferred.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 456-7890'),
('Dentist', 'Dental', 'Dentistry', 'Mid-Level', 'Houston', 'Full-Time', '$120,000 - $180,000', 'Seeking a compassionate Dentist.', 'DDS or DMD, dental license.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 567-8901'),
('Dentist', 'Dental', 'Dentistry', 'Entry-Level', 'Boston', 'Part-Time', '$90,000 - $130,000', 'Entry-level Dentist position available.', 'DDS or DMD, dental license required.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 678-9012'),
('Cardiologist', 'Cardiology', 'Cardiology', 'Senior', 'Chicago', 'Full-Time', '$200,000 - $250,000', 'Seeking an experienced Cardiologist.', 'Medical degree, board certification in cardiology, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 789-0123'),
('Cardiologist', 'Cardiology', 'Cardiology', 'Mid-Level', 'Seattle', 'Full-Time', '$180,000 - $220,000', 'Join our cardiology team.', 'Medical degree, board certification in cardiology, 3+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 890-1234'),
('Cardiologist', 'Cardiology', 'Cardiology', 'Entry-Level', 'Atlanta', 'Part-Time', '$150,000 - $190,000', 'Entry-level Cardiologist position.', 'Medical degree, board certification.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 901-2345'),
('General', 'General Medicine', 'Family Medicine', 'Senior', 'Dallas', 'Full-Time', '$180,000 - $220,000', 'Provide comprehensive medical care to patients.', 'MD degree, family medicine residency, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 012-3456'),
('General', 'General Medicine', 'Family Medicine', 'Mid-Level', 'Los Angeles', 'Full-Time', '$160,000 - $200,000', 'Looking for a dedicated General Practitioner.', 'MD degree, family medicine residency, 3+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 123-4567'),
('General', 'General Medicine', 'Family Medicine', 'Entry-Level', 'Miami', 'Part-Time', '$130,000 - $170,000', 'Entry-level General Practitioner position.', 'MD degree, family medicine residency.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 234-5678'),
('Brain and Nerves', 'Neurology', 'Neurology', 'Senior', 'Seattle', 'Full-Time', '$250,000 - $300,000', 'Join our neurology team.', 'Medical degree, fellowship in neurology, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 345-6789'),
('Brain and Nerves', 'Neurology', 'Neurology', 'Mid-Level', 'Chicago', 'Full-Time', '$220,000 - $270,000', 'Mid-level neurologist needed.', 'Medical degree, fellowship in neurology, 3+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 456-7890'),
('Brain and Nerves', 'Neurology', 'Neurology', 'Entry-Level', 'Houston', 'Part-Time', '$190,000 - $230,000', 'Entry-level position for a Neurologist.', 'Medical degree, fellowship in neurology.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 567-8901'),
('Orthopedics', 'Orthopedics', 'Orthopedic Surgery', 'Senior', 'Miami', 'Full-Time', '$250,000 - $300,000', 'Senior Orthopedic Surgeon needed.', 'MD degree, orthopedic residency, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 678-9012'),
('Dentist', 'Dental', 'Dentistry', 'Senior', 'Dallas', 'Full-Time', '$180,000 - $220,000', 'Senior Dentist needed for private practice.', 'DDS or DMD, extensive experience required.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 789-0123'),
('Cardiologist', 'Cardiology', 'Cardiology', 'Senior', 'Atlanta', 'Full-Time', '$230,000 - $280,000', 'Looking for a skilled Cardiologist.', 'MD degree, board certification, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 890-1234'),
('General', 'General Medicine', 'Family Medicine', 'Senior', 'Boston', 'Full-Time', '$190,000 - $240,000', 'Senior General Practitioner needed.', 'MD degree, family medicine residency, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 901-2345'),
('Brain and Nerves', 'Neurology', 'Neurology', 'Senior', 'San Francisco', 'Full-Time', '$250,000 - $300,000', 'Experienced Neurologist wanted.', 'Medical degree, fellowship in neurology, 5+ years of experience.', NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 'hr@hospital.com', '(555) 012-3456')
'''

try:
    cursor.execute(insert_data_query)
    conn.commit()
    print("Sample data inserted into 'MedicalJobs' successfully.")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
