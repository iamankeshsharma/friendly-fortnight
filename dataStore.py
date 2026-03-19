import json

class DataStore:
    def __init__(self):
        
        with open('data.json', 'r') as file:
            self.data = json.load(file)

    def get(self, key):
        return self.data.get(key, None)

