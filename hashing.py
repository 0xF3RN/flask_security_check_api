import hashlib


class Hasher:
    def __init__(self, usr, pswd):
        self.usr = usr
        self.pswd = pswd

    def get_hash(self):
        data_salted = self.usr + self.pswd + self.usr
        hashed_pswd = hashlib.md5(data_salted.encode('utf-8')).hexdigest()
        return hashed_pswd
