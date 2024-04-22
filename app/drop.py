from pymongo import MongoClient
from os import getenv

import certifi
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame  # type: ignore
from pymongo import MongoClient

# Connect to MongoDB
load_dotenv()
client = MongoClient(getenv("DB_URL"), tlsCAFile=certifi.where())

# Access the database
db = client["monster_db"]

# Drop a specific collection
collection = db["monsters"]
collection.delete_many({})

# Drop the entire database
#client.drop_database("your_database_name")

# Close the connection
client.close()