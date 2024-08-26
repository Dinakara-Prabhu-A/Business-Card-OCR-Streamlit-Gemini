from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image
import pandas as pd
from ocr import get_gemini_response
from utils.helper import image_to_base64,base64_to_image
from db import create_table,insert_record,update_record_by_name,delete_record_by_name,retrieve_names,get_record_by_name_df
import json
import pandas as pd

def main():
    # page configration

    st.set_page_config(page_title = "BizCardX",page_icon="images.png",layout ='centered')
    st.title('BizCardX')
    option = option_menu(
        menu_title=None,
        options=["Extract Info", "View Data"],
        icons=["cloud-upload", "database"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal" )
    create_table()
    if option == "Extract Info":
        st.header("Extract Information")
        # image upload
        uploaded_file = st.file_uploader("Upload your business card image", type=["png", "jpg",'jpeg'])
    
    
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            with st.popover("Image",use_container_width=True):
                st.image(image, caption="Image uploaded")
            response = get_gemini_response(image)
            response = json.loads(response)
            response['Image']= image_to_base64(image)
            # Function to handle lists and convert them to comma-separated strings
            def convert_to_string(value):
                if isinstance(value, list):
                    return ', '.join(map(str, value))  # Join list elements with commas
                return value

            # Create a container to display the extracted data
            container = st.container()


            # Convert the cleaned response to DataFrame
            response_cleaned = {k: convert_to_string(v) if k != "image" else v for k, v in response.items()}
            columns = list(response.keys())
            df = pd.DataFrame([response_cleaned],columns=columns)  # Make sure it's in list format for DataFrame

            st.write("Data as DataFrame:")
            st.dataframe(df)
            # Save extracted data to a database
            if st.button("Save to Database"):
                # Save the data to the database (handled in db.py)
                
                insert_record(company_name=df['Company Name'].iloc[0],name= df['Name'].iloc[0], designation=df['Designation'].iloc[0], mobile_number= df['Mobile Number'].iloc[0], email_address=df['Email Address'].iloc[0], 
                               website_url =df['Website URL'].iloc[0], area =df["Area"].iloc[0], city=df['City'].iloc[0], state=df['State'].iloc[0], pin_code=df['Pin Code'].iloc[0],image = response['Image'])
                st.success("Data saved successfully!")
                
    elif option == "View Data":
        st.header("View Data")
        # Retrieve the names of all records
        record_names = retrieve_names()
        # Select a record to view
        selected_record = st.selectbox("Select a record to view", record_names, index=None, placeholder="-- Option --")
        
        if selected_record:
            # Retrieve the selected record
            record = get_record_by_name_df(selected_record)
            
            st.write("Record Details:")
            # Display the selected record details
            st.dataframe(record.iloc[:,:-1])
            image = record['Image'].iloc[0]
            image =  base64_to_image(image)
            with st.popover("Image",use_container_width=True):
                st.image(image, caption="Image")
            
            # Main container to organize the update fields
            main_container = st.container(border=True)
            
            # Columns for the input fields
            c1, c2, c3 = main_container.columns(3)
            
            # Text inputs to update the record
            with c1:
                container = st.container(border=True)
                company_name = container.text_input("Company Name", record['Company Name'].iloc[0])
            with c2:
                container = st.container(border=True)
                designation = container.text_input("Designation", record['Designation'].iloc[0])
            with c3:
                container = st.container(border=True)
                mobile = container.text_input("Mobile Number", record['Mobile Number'].iloc[0])
            with c1:
                container = st.container(border=True)
                email = container.text_input("Email Address", record['Email Address'].iloc[0])
            with c2:
                container = st.container(border=True)
                url = container.text_input("Website URL", record['Website URL'].iloc[0])
            with c3:
                container = st.container(border=True)
                area = container.text_input("Area", record['Area'].iloc[0])
            with c1:
                container = st.container(border=True)
                city = container.text_input("City", record['City'].iloc[0])
            with c2:
                container = st.container(border=True)
                state = container.text_input("State", record['State'].iloc[0])
            with c3:
                container = st.container(border=True)
                pincode = container.text_input("Pin Code", record['Pin Code'].iloc[0])
            

            col1,col2 ,col3= st.columns(3)
            with col1:
                # Update button
                update_button = st.button("Update the database",use_container_width=True)
                
                # If the update button is clicked
            if update_button:
                # Collect the updated values into a dictionary
                update_values = {
                    'company_name': company_name,
                    'designation': designation,
                    'mobile_number': mobile,
                    'email_address': email,
                    'website_url': url,
                    'area': area,
                    'city': city,
                    'state': state,
                    'pin_code': pincode
                }
                
                # Update the record in the database
                update_record_by_name(name=selected_record, new_data=update_values)
                
                # Show a success message
                st.success("Record updated successfully!")
                st.write("Please click refresh to see updated information")
                
            with col2:
                # Delete button
                delete_button = st.button("Delete the database",use_container_width=True)
                
                # If the delete button is clicked
            if delete_button:
                # Delete the record from the database
                delete_record_by_name(name=selected_record)
                
                # Show a success message
                st.success("Record deleted successfully!")
                st.write("Please click refresh to see updated information")
                    
            with col3:
                # Refresh button
                refresh_button = st.button("Refresh",use_container_width=True)
                
                # If the refresh button is clicked
                if refresh_button:
                    # Refresh the page
                    st.rerun()        
                    
main()