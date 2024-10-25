from .abstraction import AbsteractionDataAccess


class MockDataAccess(AbsteractionDataAccess):
    def __init__(self,data_access):
        self.data_access=data_access
    def create_auth(self,email,password):
        pass
    def get_auth(self,auth_id):
        pass
    def delete_auth(self,auth_id):
        pass

        