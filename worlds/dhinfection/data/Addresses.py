from abc import ABC
from typing import Dict

from .Strings import ItemNames, EventNames, PlayStatNames


class VolumeAddresses(ABC):
    Items: Dict[ItemNames, int]
    Events: Dict[EventNames, int]
    PlayStats: Dict[PlayStatNames, int]
    AreaWords: int
    WordLists: int
    Storage: int
    Party: int


class InfectionVolumeAddresses(VolumeAddresses):
    AreaWords = 0xa44c0c
    WordLists = 0xa44c47
    Storage = 0xa40543
    Party = 0xa41bf0

    Items = {
        ItemNames.VirusCoreA: 0xa406cc,
        ItemNames.VirusCoreB: 0xa406cd,
        ItemNames.VirusCoreC: 0xa406ce,
        ItemNames.RyuBookI: 0xA407DD,
        ItemNames.RyuBookII: 0xA407DE,
        ItemNames.RyuBookIII: 0xA407DF,
        ItemNames.RyuBookIV: 0xA407E0,
        ItemNames.RyuBookV: 0xA407E1,
        ItemNames.RyuBookVI: 0xA407E2,
        ItemNames.RyuBookVII: 0xA407E3,
        ItemNames.RyuBookVIII: 0xA407E4,
    }
    Events = {
        EventNames.Stehony: 0xa45059,
        EventNames.Jonue: 0xa45061,
        EventNames.Zyan: 0xa45069,
        EventNames.Albert: 0xa45071,
        EventNames.Martina: 0xa45079,
        EventNames.Sanjuro: 0xa45099,
        EventNames.Gardenia: 0xa450a2,
        EventNames.Natsume: 0xa450b0,
        EventNames.GracefulBook: 0xa450a9,
    }
    PlayStats = {
        PlayStatNames.AreasVisited: 0xa46232,
        PlayStatNames.AllFieldPortalsOpened: 0xa46236,
        PlayStatNames.AllDungeonPortalsOpened: 0xa46238,
        PlayStatNames.PortalsOpened: 0xa46234,
        PlayStatNames.ChestsOpened: 0xa46e10,
        PlayStatNames.BreakablesBroken: 0xa46e12,
        PlayStatNames.GottOpened: 0xa46e3e,
        PlayStatNames.SymbolsActivated: 0xa46e14,
        PlayStatNames.TotalDataDrains: 0xa4622e,
        PlayStatNames.KiteLevel: 0xa46e66,
    }
