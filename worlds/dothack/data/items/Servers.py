from enum import Enum
from BaseClasses import Item, ItemClassification


class Servers(Enum):
    @classmethod
    def from_id(self, id: int):
        for member in self:
            if member.value["id"] == id:
                return member
        return None
    Delta = {"id": 0, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Theta = {"id": 1, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Lambda = {"id": 2, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Sigma = {"id": 3, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Omega = {"id": 4, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
