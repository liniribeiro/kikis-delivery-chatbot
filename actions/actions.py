import json
import os
from typing import Any, Text, Dict, List

import requests
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

load_dotenv()

airtable_api_key = os.getenv("AIRTABLE_API_KEY")
base_id = os.getenv("BASE_ID")
table_name = os.getenv("TABLE_NAME")


def create_health_log(name, message):
    request_url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

    headers = {
        "Content-Type": "application/json",
        "Accept":  "application/json",
        "Authorization": f"Bearer {airtable_api_key}"
    }

    data = {
        "fields": {
            "name": name,
            "message": message,
        }
    }

    try:
        response = requests.post(
            request_url, headers=headers, data=json.dumps(data)
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    print(response.status_code)
    return response


class DemoFormSubmit(Action):

    def name(self) -> Text:
        return "delivery_from_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        create_health_log(tracker.get_slot('name'),
                          tracker.get_slot('message'))

        dispatcher.utter_message(text="Prontinho, enviei seu recado para a Alini!")

        return []