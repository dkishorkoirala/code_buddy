# TODO: Import the TextFile class from textfile.py
from textfile import TextFile
from database import Database
from networkresource import NetworkResource

# TODO: Import the Database class from database.py
# TODO: Import the NetworkResource class from networkresource.py

def process_data(data_source, data):
    # TODO: Call the read() method on data_source and print the result
    # TODO: Call the write(data) method on data_source and print the result
    print(data_source.read())
    print(data_source.write(data))


# Test with different data sources - DO NOT MODIFY THIS TEST CODE
text_file = TextFile()
database = Database()
network = NetworkResource()

print("Processing text file:")
process_data(text_file, "Hello, world!")

print("\
Processing database:")
process_data(database, "User record")

print("\
Processing network resource:")
process_data(network, "GET request")