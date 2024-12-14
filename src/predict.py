import pandas as pd
import pickle
from custom_transformer import TitleCreation
import json

class Predict:
    def generate_predictions(self, path):
        model = pickle.load(open("my_final_solution.pickle", "rb"))
        with open(path, "r") as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        return model.predict_proba(df)



if __name__ == "__main__":
    print(Predict().generate_predictions("mock_data.json"))
