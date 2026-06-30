from enum import Enum
from typing import TypedDict
from BaseClasses import ItemClassification


class PartyMemberAttributes(TypedDict):
    id: int
    classifications: dict[int, ItemClassification]
    volumes: list[int]


class PartyMembers(Enum):
    _value_: PartyMemberAttributes

    @classmethod
    def from_id(self, id: int):
        for member in self:
            if member.value["id"] == id:
                return member
        return None
    Mia = {"id": 1, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Orca = {"id": 2, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Marlo = {"id": 3, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Sanjuro = {"id": 4, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    NukeUsagimaru = {"id": 5, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Balmung = {"id": 6, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Moonstone = {"id": 7, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Piros = {"id": 8, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Wiseman = {"id": 9, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Elk = {"id": 10, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Natsume = {"id": 11, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Rachel = {"id": 12, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    Gardenia = {"id": 13, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    TerajimaRyoko = {"id": 14, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
    BlackRose = {"id": 15, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Mistral = {"id": 16, "classifications": {1: ItemClassification.progression}, "volumes": [1]}
    Helba = {"id": 17, "classifications": {1: ItemClassification.useful}, "volumes": [1]}
