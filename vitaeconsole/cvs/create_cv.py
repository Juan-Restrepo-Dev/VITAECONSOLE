import json

 
def add_cv_to(cv):
    try:
        with open('../db.json', 'r') as f:
            db = json.load(f)
            db["cvs"].append(cv)
        with open('db.json', 'w') as f:
            json.dump(db, f, indent=4)  

    except FileNotFoundError:
        print("The JSON file was not found.")

    except json.JSONDecodeError:
        print("The JSON file is not valid.")




    