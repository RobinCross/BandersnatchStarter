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
        """
        Seed function generate a specified number of monsters from the MonstersLab library
        and insert them into the monster's collection.
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)

    def reset(self):
        """
        Reset function deletes all monsters from the monsters collection
        """
        self.collection.delete_many({})

    def count(self) -> int:
        """
        The Count function returns the number of monsters in the monsters collectiongit
        """
        self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        data = list(self.collection.find({}), {"_id": False})

    def html_table(self) -> str:
        df = self.dataframe()
        return df.to_html(index=False) if not df.empty else ""
