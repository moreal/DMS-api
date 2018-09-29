class Account():
    def __init__(self, id: str, pw: str):
        account.id = id
        account.pw = pw
        account.refresh_token = None

    def login(self):
        from dms.v2.student.auth import login
        login(self)

