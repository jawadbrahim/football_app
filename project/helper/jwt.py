import jwt

class JwtHelper:
    def __init__(self, algorithm, secret):
        self.algorithm = algorithm
        self.secret = secret

    def encode(self, payload):
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def decode(self, token):
        return jwt.decode(token, self.secret, algorithms=[self.algorithm])
