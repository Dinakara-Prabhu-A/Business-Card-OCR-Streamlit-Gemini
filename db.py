import sqlite3
import pandas as pd
# Function to create the table (without id column)
def create_table():
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS business_cards (
                 company_name TEXT,
                 name TEXT PRIMARY KEY,
                 designation TEXT,
                 mobile_number TEXT,
                 email_address TEXT,
                 website_url TEXT,
                 area TEXT,
                 city TEXT,
                 state TEXT,
                 pin_code TEXT,
                 image BLOB)''')
    
    conn.commit()
    conn.close()

# Function to insert a new record
def insert_record(company_name, name, designation, mobile_number, email_address, 
                  website_url, area, city, state, pin_code,image):
    
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()

    # Check if the record with the given name already exists
    c.execute("SELECT * FROM business_cards WHERE name = ?", (name,))
    existing_record = c.fetchone()

    if existing_record:
        # If the record exists, update it
        c.execute('''UPDATE business_cards SET company_name = ?, designation = ?, 
                    mobile_number = ?, email_address = ?, website_url = ?, area = ?, 
                    city = ?, state = ?, pin_code = ? ,image =? WHERE name = ?''',
                  (company_name, designation, mobile_number, email_address, 
                   website_url, area, city, state, pin_code,image, name))
    else:
        # If the record does not exist, insert a new one
        c.execute('''INSERT INTO business_cards (company_name, name, designation, mobile_number, 
                    email_address, website_url, area, city, state, pin_code, image) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (company_name, name, designation, mobile_number, email_address, 
                   website_url, area, city, state, pin_code,image))
    
    conn.commit()
    conn.close()

# Function to retrieve all records of 'name'
def retrieve_names():
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    c.execute("SELECT name FROM business_cards")
    names = c.fetchall()
    
    conn.close()
    return [name[0] for name in names]

# Function to delete a record based on the 'name'
def delete_record_by_name(name):
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM business_cards WHERE name = ?", (name,))
    
    conn.commit()
    conn.close()

# Function to update a record based on 'name' (without image)
def update_record_by_name(name, new_data):
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    c.execute('''UPDATE business_cards SET company_name = ?, designation = ?, mobile_number = ?, 
                email_address = ?, website_url = ?, area = ?, city = ?, state = ?, pin_code = ?
                WHERE name = ?''',
              (new_data['company_name'], new_data['designation'], new_data['mobile_number'], 
               new_data['email_address'], new_data['website_url'], new_data['area'], 
               new_data['city'], new_data['state'], new_data['pin_code'], name))
    
    conn.commit()
    conn.close()

def retrieve_all_records():
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM business_cards")
    names = c.fetchall()
    
    conn.close()
    return names

def get_record_by_name_df(name):
    conn = sqlite3.connect('business_card.db')
    c = conn.cursor()
    
    # Fetch the record where the name matches the input
    c.execute("SELECT * FROM business_cards WHERE name = ?", (name,))
    record = c.fetchall()
    
    conn.close()
    
    # Define the column names for the DataFrame, including the image column
    columns = ['Company Name', 'Name', 'Designation', 'Mobile Number', 'Email Address',
               'Website URL', 'Area', 'City', 'State', 'Pin Code','Image']
    
    # Check if any records exist
    if record:
        # Create DataFrame from the fetched record(s)
        df = pd.DataFrame(record, columns=columns)
        return df
    else:
        return f"No record found for the provided name : {name}"
