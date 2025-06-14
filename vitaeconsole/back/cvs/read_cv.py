import json

import os

# Open and read the JSON file
def read_db():
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory+"/db.json")
    Data:list
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            Data = json_data["cvs"] 
            # Print the data
        return Data

    except FileNotFoundError:
        print("The JSON file was not found.")

    except json.JSONDecodeError:
        print("The JSON file is not valid.")