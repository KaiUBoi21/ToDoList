#mvp
# 1. Ability for user to save to database
# 2. Ability for a user to see all items in the database

import json
from datetime import datetime 
def user_input():
    """
    function that takes a ToDo list input and returns a dictionary of the item

    """
    title = input("Enter title of item: ")
    description = input("Enter item description: ")
    date_created = datetime.today().strftime('%Y-%m-%d')
    due_date = input("Enter in the date in format Year-Month-Date: ") #TODO: validate this input
    itemdict = {
        "title":title,
        "description":description,
        "date_created:":date_created,
        "due_date":due_date
    }
    return itemdict

def save_entry(entry: dict):
    """
    Function to write to our database
    Step 1: Open our database in reading mode and save the entire db to a variable called data
    Step 2: Append the new entry to the data variable
    Step 3: Save the new variable and write it back to the db
    """
    with open("db.json", "r") as file:
        data = json.load(file)
    data.append(entry)
    with open("db.json", "w") as file:
        json.dump(data, file)








if __name__ == "__main__":
    main()
