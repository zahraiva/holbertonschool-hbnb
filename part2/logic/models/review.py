from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating):
        super().__init__()
        self.text = text
        self.rating = rating
