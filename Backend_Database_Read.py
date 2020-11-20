import sqlite3

# Read data from database for SVM evaluation and user input prediction
def read_train_test_data():

    # Create database or connect to one
    connection = sqlite3.connect('smart_product.db')

    # Create cursor instance
    c = connection.cursor()

    # Create query
    c.execute("SELECT * FROM train_test_data")
    train_test_data = c.fetchall()
    # print(len(train_test_data))
    # Commit changes
    connection.commit()

    # Close connection
    connection.close()

    return train_test_data

