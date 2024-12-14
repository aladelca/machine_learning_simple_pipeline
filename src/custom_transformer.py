import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class TitleCreation(TransformerMixin, BaseEstimator):
    def __init__(self, column):
        self.column = column
    def fit_transform(self, x: pd.DataFrame, y = None):
        x_copy = x.copy()
        equivalences = {
                        "Mr": "Mr" ,
                        "Mrs": "Mrs",
                        "Miss": "Ms",
                        "Master": "Academic",
                        "Don": "Royalty",
                        "Rev": "Royalty",
                        "Dr": "Academic",
                        "Mme": "Mrs",
                        "Ms": "Ms",
                        "Major" : "Military",
                        "Lady": "Royalty",
                        "Sir": "Royalty",
                        "Mlle": "Ms",
                        "Col": "Military",
                        "Capt": "Military",
                        "the Countess": "Royalty",
                        "Jonkheer": "Royalty"
                    }
        def cleaning_text(text):
            start = text.find(",")
            end = text.find(".")
            return text[start+2:end]
        x_copy[self.column] = x_copy[self.column].apply(cleaning_text).map(equivalences)
        return x_copy[[self.column]]

    def fit(self, x: pd.DataFrame, y = None):
        return self
    def transform(self, x: pd.DataFrame, y = None):
        return self.fit_transform(x)