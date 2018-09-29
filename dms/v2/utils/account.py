class Account():
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        self.jwt = None

    def login(self):
        id, pw = self.id, self.pw

        import requests
        from config import DMS_URL
        
        resp = requests.post(
            url=f"http://{DMS_URL}/v2/student/auth",
            json={'id': id, 'pw': pw})

        resp.text

        