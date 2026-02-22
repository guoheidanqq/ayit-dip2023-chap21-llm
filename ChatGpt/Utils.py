import json

class Utils:
    def __init__(self):
        pass
    
    
    @staticmethod
    def loadJson(filePath):
        with open(filePath) as f:
            return json.load(f)