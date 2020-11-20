import sqlite3

def backend_create_new_database():
    # Create database or connect to one
    connection = sqlite3.connect('smart_product.db')

    # Create cursor instance
    c = connection.cursor()
        
    # Create table. Use only in case if you would like to set up a new table
    c.execute("""CREATE TABLE train_test_data (

        sensing real, acting_own real, acting_inter real, 
        autonomy real, direction real, multiplicity real, 
        partner_user real, partner_business real, partner_thing real, 
        source_state real, source_context real, source_usage real, source_cloud real, 
        data_usage real, 
        offline_func real, value_proposition real, ecosystem real, cluster real, success_class real 
        )""")

    # Print column names. Uncomment to comprehend if database creation was successfully
    # c.execute("SELECT * FROM train_test_data")
    # Print column names. Uncomment to comprehend if database creation was successfully
    # col_name_list = [tuple[0] for tuple in c.description]
    # print(col_name_list)

    # Commit changes
    connection.commit()

    # Close connection
    connection.close()