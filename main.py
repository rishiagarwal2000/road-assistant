import requests
from typing import Optional, List
from dotenv import load_dotenv
import os

import together
import openai
import json

load_dotenv()
google_api_key = os.getenv('google_api_key')

def get_nearby_places(lat : float = 37.7937, long : float = -122.3965, fields : Optional[List[str]] = None):
    if fields is None:
        fields = ["displayName", "editorialSummary"]
    
    fields = ["places." + field for field in fields]

    url = "https://places.googleapis.com/v1/places:searchNearby"
    query = {
            "includedTypes": ["restaurant"],
            "maxResultCount": 10,
            "locationRestriction": {
                "circle": {
                "center": {
                    "latitude": lat,
                    "longitude": long},
                "radius": 500.0
                }
            }
        }
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": google_api_key,
        "X-Goog-FieldMask": ",".join(fields)
    }
    response = requests.post(url, data=query, headers=headers)

    return response