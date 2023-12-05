from typing import Any, Text, Dict, List
import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenreEntity(Action):

    def name(self) -> Text:
         return "action_genre_entity"
         
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        csv_file_path = "/Users/Elisabeth/Downloads/archive/IMDB-Movie-Data.csv"
        df = pd.read_csv(csv_file_path, header=0)
 
        genre_entity_original = next(tracker.get_latest_entity_values("genre"), None)
        genre_entity = genre_entity_original.lower()
        
        df["Genre"] = df["Genre"].apply(lambda x: x.lower())

        #filtered_df = df[df["Genre"] == genre_entity]
        filtered_df = df[df["Genre"].apply(lambda genres: genre_entity in genres)]

        if not filtered_df.empty:
            recommended_movie = filtered_df.sample()["Title"].values[0]
            dispatcher.utter_message(template="utter_movie_recommendation", movie=recommended_movie, genre=genre_entity)
        else:
            dispatcher.utter_message(template="utter_unknown_genre")

        return[]
