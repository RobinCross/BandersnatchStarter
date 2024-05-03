from os import getenv

import certifi
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame  # type: ignore
from pymongo import MongoClient


class Database:
    def __init__(self):
        load_dotenv()  # Load environmental variables from the .env file
        self.client = MongoClient(getenv("DB_URL"), tlsCAFile=certifi.where())
        # Creates a Mongo Client from the pymongo library and creates a connection to the mongodb cluster
        self.db = self.client["monster_db"]
        # Get a reference to the monster_db database in mongodb
        self.collection = self.db["monsters"]
        # Get a reference to the monsters collection within the monster_db database
    def set_db_url(self, db_url):
        self.client = MongoClient(db_url, tlsCAFile=certifi.where())
        self.db = self.client["monster_db"]
        self.collection = self.db["monsters"]

    def seed(self, amount):
        """
        Seed method generate a specified number of monsters from the MonstersLab library
        and inserts them into the monster's collection.
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)

    def reset(self):
        """
        Reset method deletes all monsters from the monsters collection
        """
        self.collection.delete_many({})

    def count(self) -> int:
        """
        The Count method returns the number of monsters in the monsters collection
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        The dataframe method retrieves all the docs from the monsters collection using find()
        with an empty filter {} and excludes the _id field using "_id:":False.
        """
        data = list(self.collection.find({}, {"_id": False}))
        return DataFrame(data)

    def html_table(self) -> str:
        """
        The html method calls the dataframe method to get the data. If the dataframe is not
        empty it converts it to an HTML table, and excludes the row index.
        If the dataframe is empty it returns an empty string.
        """
        df = self.dataframe()
        return df.to_html(index=False) if not df.empty else ""


# allows me to run the script directly
if __name__ == "__main__":
    # create an instance of the Database class
    db = Database()
    # Reset the data within the database
    db.reset()
    # Generate 10 monsters into the database
    db.seed(10)
    print(f"Number of monsters: {db.count()}")
    print(db.dataframe())
