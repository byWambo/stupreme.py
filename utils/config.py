import os
import json


class Config:
    def __init__(self, path="config.json"):
        self.path = path
        self.params = {
            "token": "Enter the token of your bot",
            "prefix": "Enter the default prefix",
            "owner_id": "Enter the id of the owner"
        }

    def create(self):
        if not os.path.isfile(self.path):
            with open(self.path, "w") as file:
                json.dump(self.params, file, indent=4)
                print("Config file has been created, please fill out the config and restart!")
                exit(0)
        else:
            with open(self.path, "r") as file:
                self.params = json.load(file)

        return self.params
