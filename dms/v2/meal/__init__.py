import datetime
import requests
import json

from dms.v2.config import DMS_URL


class Meal():
    @staticmethod
    def get(date: datetime.date or str=datetime.date.today()):
        if not isinstance(date, str):
            date = str(date)

        resp = requests.get(f"http://{DMS_URL}/v2/meal/{date}")

        meals = json.loads(resp.text)

        return meals['breakfast'], meals['lunch'], meals['dinner']
