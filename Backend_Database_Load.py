import csv
import sqlite3
from tkinter import messagebox # For confirmation if data was successfully loaded

# Function opens csv-file to write the smart product data into the related table. Necessary for training SVM and predicting smart product success
def load_data_into_database():
    
    with open("Smart_Product_Data_float_ex_fitbit.csv", mode="r") as smart_product_data:

        smart_product_data_reader = csv.reader(smart_product_data, delimiter=",") # CSV reader
        
        next(smart_product_data_reader, None)     # Skip the header, since column names are already available
        
        # Create database or connect to one
        connection = sqlite3.connect('smart_product.db')

        # Create cursor instance
        c = connection.cursor()
        
        # Write values into table
        c.executemany("""INSERT INTO train_test_data VALUES(
            :sensing , :acting_own , :acting_inter , 
            :autonomy , :direction , :multiplicity , 
            :partner_user , :partner_business , :partner_thing , 
            :source_state , :source_context , :source_usage , :source_cloud , 
            :data_usage , 
            :offline_func , :value_proposition , :ecosystem , :cluster , :success_class 
            )""", smart_product_data_reader)

        # Print column names and values. Uncomment to comprehend if writing into database was successfully
        # c.execute("SELECT * FROM train_test_data")
        # col_name_list = [tuple[0] for tuple in c.description]
        # print(col_name_list)
        # db_values = c.fetchall()
        # print(db_values)

        # Commit changes
        connection.commit()

        # Close connection
        connection.close()

        # Confirmation, if data was successfully loaded
        messagebox.showinfo(title="Confirmation", message = "Data successfully loaded!")
    
