import requests
import json

from dms.v2.student import Account
from dms.v2.config import DMS_URL


def get_tokens_from_response(content: requests.Response) -> (str, str):
    tokens = json.loads(resp.text)
    return tokens['refreshToken'], tokens['accessToken']


def login(account: Account) -> bool:
    resp = requests.post(
        url=f"http://{DMS_URL}/v2/student/auth",
        json={'id': account.id, 'password': account.pw})

    if resp.status_code == 1:
        pass

    account.refresh_token, account.access_token = get_tokens_from_response(resp)
