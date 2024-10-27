from storage.in_memory_repository import InMemoryRepository

class Facade:
    def __init__(self):
        self.repository = InMemoryRepository()

    def add_item(self, item_id, item):
        self.repository.add(item_id, item)

    def get_item(self, item_id):
        return self.repository.get(item_id)

    def remove_item(self, item_id):
        self.repository.remove(item_id)
