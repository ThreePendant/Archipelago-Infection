from abc import ABC
from typing import Dict

from .Strings import ItemNames, EventNames, PlayStatNames


class VolumeAddresses(ABC):
    Items: Dict[ItemNames, int]
    Events: Dict[EventNames, int]
    PlayStats: Dict[PlayStatNames, int]


class InfectionVolumeAddresses(VolumeAddresses):
    Items = {

    }
    Events = {

    }
    PlayStats = {

    }
