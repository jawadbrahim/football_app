import bcrypt

class HashingHelper:
    def hash_password(self,value):
        salt=bcrypt.gensalt()
        hashed=bcrypt.hashpw(value.encode('utf-8'),salt)
        return hashed.decode('utf-8')
    def verify_password(self,provided_password,stored_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'),stored_password.encode('utf-8'))