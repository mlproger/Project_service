class MyExseption(Exception):
    def __init__(self, staus_code: int, msg: str):
        self.msg = msg
        self.status_code = staus_code
