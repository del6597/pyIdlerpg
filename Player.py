import json

class PlayerJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return {"Name": obj.name, "Idled": obj.idled}
        return json.JSONEncoder.defauilt(self, obj)

class Player():
    def __init__(self):
        pass
