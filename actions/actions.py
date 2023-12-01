from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenreEntity(Action):

    def name(self) -> Text:
         return "action_genre_entity"
         
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        genre_entity = next(tracker.get_latest_entity_values("genre"), None)

        if genre_entity:
            dispatcher.utter_message(template=f"utter_genre_chosen", genre=genre_entity)
        else:
            dispatcher.utter_message(template="utter_unknown_genre")

        return[]

class MovieChoice(Action):

    def name(self) -> Text:
         return "action_movie_choice"
         
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_genre")

        return[]