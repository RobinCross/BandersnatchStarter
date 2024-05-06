from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
import joblib


class Machine:
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        prediction = self.model.predict(pred_basis)
        probability = self.model.predict_proba(pred_basis).max()
        return prediction[0], probability

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f"{self.name} initialized at {self.timestamp}"
