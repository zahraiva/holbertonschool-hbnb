class InMemoryRepository:
    def __init__(self):
        self.storage = {}

    def add(self, item_id, item):
        if item_id in self.storage:
            raise ValueError("Item already exists.")
        self.storage[item_id] = item

    def get(self, item_id):
        return self.storage.get(item_id)

    def remove(self, item_id):
        if item_id not in self.storage:
            raise ValueError("Item does not exist.")
        del self.storage[item_id]
