from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password
        self.places = []

    def create_place(self, place):
        self.places.append(place)
