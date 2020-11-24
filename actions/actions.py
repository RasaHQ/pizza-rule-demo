from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_flush_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slots = []
        for key in ("topping", "size"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=None))
        # dispatcher.utter_message(text="The slots are now flushed.")

        return slots
