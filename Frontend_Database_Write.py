import sqlite3

# Function to write the user's smart product data into the related table
def write_to_database(_smart_object_characteristics):

    # Create database or connect to one
    connection = sqlite3.connect('smart_product.db')

    # Create cursor instance
    c = connection.cursor()
        
    c.execute("""INSERT INTO user_input VALUES (:sensing, :acting_own, :acting_inter, 
        :autonomy, :direction, :multiplicity, 
        :partner_user, :partner_business, :partner_thing, 
        :source_state, :source_context, :source_usage, :source_cloud, 
        :data_usage, 
        :offline_func, :value_proposition, :ecosystem        
    )""", _smart_object_characteristics)

    # Print column names and values. Uncomment to comprehend if writing into database was successfully
    # c.execute("SELECT * FROM user_input")
    # col_name_list = [tuple[0] for tuple in c.description]
    # print(col_name_list)
    # db_values = c.fetchall()
    # print(db_values)

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()