import requests

from dms.v2.student import Account
from dms.v2.config import DMS_URL


def apply_before(account: Account, class_no: int, seat_no: int) -> bool:
    resp = requests.post(
        url=f"http://{DMS_URL}/v2/student/apply/extension/11",
        headers=''
    )


def apply_after(account: Account, class_no: int, seat_no: int) -> bool:
    resp = requests.post(
        url=f"http://{DMS_URL}/v2/student/apply/extension/12",
        json={
            'classNum': class_no,
            'seatNum': seat_no
        }
    )