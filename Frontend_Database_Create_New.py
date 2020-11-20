import sqlite3

def frontend_create_new_database():
    # Create database or connect to one
    connection = sqlite3.connect('smart_product.db')

    # Create cursor instance
    c = connection.cursor()
        
    # Create table. Use in case if you would like to set up a new table
    c.execute("""CREATE TABLE user_input (

        sensing integer, acting_own real, acting_inter real, 
        autonomy real, direction integer, multiplicity integer, 
        partner_user real, partner_business real, partner_thing real, 
        source_state real, source_context real, source_usage real, source_cloud real, 
        data_usage real, 
        offline_func integer, value_proposition integer, ecosystem real
        )""")

    # Print column names. Uncomment to comprehend if database creation was successfully
    # c.execute("SELECT * FROM user_input")
    # Print column names. Uncomment to comprehend if database creation was successfully
    # col_name_list = [tuple[0] for tuple in c.description]
    # print(col_name_list)

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()