from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    def __int__(self):
        load_dotenv()
        self.client = MongoClient(getenv("DB_URL"))
        self.db = self.client["monster_db"]
        self.collection = self.db["monsters"]



    def seed(self, amount):
        monsters = [Monster().to_dict() for _ in range(amount)]
        result = self.collection.insert_many(monsters)
        print(f"Inserted {len(result.inserted_ids)} monsters into the database.")



    def reset(self):
        pass

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass
