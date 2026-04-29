from enum import Enum
from BaseClasses import ItemClassification
from ..items.AreaWords import AreaWords
from ..Strings import AreaWordNames


class WordListBase(Enum):
    @classmethod
    def from_address(self, address: int):
        for member in self:
            if member.value["address"] == address:
                return member
        return None


def get_wordlist_name(wordlist: WordListBase) -> str:
    words = []
    for word in wordlist.value["words"]:
        words.append(AreaWordNames[word.name].value)
    return " ".join(words)


class InfectionDeltaWordList(WordListBase):
    BurstingPassedOverAquaField = {"address": 0x0e, "words": [
        AreaWords.Bursting, AreaWords.PassedOver, AreaWords.AquaField
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    HiddenForbiddenHolyGround = {"address": 0x0f, "words": [
        AreaWords.Hidden, AreaWords.Forbidden, AreaWords.HolyGround
    ],
        "classifications": {1: ItemClassification.useful},
        "volumes": [1]
    }
    HideousSomeonesGiant = {"address": 0x10, "words": [
        AreaWords.Hideous, AreaWords.Someones, AreaWords.Giant
    ],
        "classifications": {1: ItemClassification.useful},
        "volumes": [1]
    }
    ExpansiveHauntedSeaOfSand = {"address": 0x11, "words": [
        AreaWords.Expansive, AreaWords.Haunted, AreaWords.SeaOfSand
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    BoundlessCorruptedFortWalls = {"address": 0x12, "words": [
        AreaWords.Boundless, AreaWords.Corrupted, AreaWords.FortWalls
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    ClosedObliviousTwinHills = {"address": 0x13, "words": [
        AreaWords.Closed, AreaWords.Oblivious, AreaWords.TwinHills
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DetestableGoldenSunnyDemon = {"address": 0x1c, "words": [
        AreaWords.Detestable, AreaWords.Golden, AreaWords.SunnyDemon
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DiscoveredPrimitiveTouchstone = {"address": 0x1d, "words": [
        AreaWords.Discovered, AreaWords.Primitive, AreaWords.Touchstone
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    IndiscreetGluttonousPilgrimage = {"address": 0x1e, "words": [
        AreaWords.Indiscreet, AreaWords.Gluttonous, AreaWords.Pilgrimage
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DetestableGoldenMessenger = {"address": 0x27, "words": [
        AreaWords.Detestable, AreaWords.Golden, AreaWords.Messenger
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    RagingPassionateMelody = {"address": 0x23, "words": [
        AreaWords.Raging, AreaWords.Passionate, AreaWords.Melody
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    PlenteousSmilingHypha = {"address": 0x15, "words": [
        AreaWords.Plenteous, AreaWords.Smiling, AreaWords.Hypha
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DetestableGoldenScent = {"address": 0x28, "words": [
        AreaWords.Detestable, AreaWords.Golden, AreaWords.Scent
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    HideousDestroyersFarThunder = {"address": 0x20, "words": [
        AreaWords.Hideous, AreaWords.Destroyers, AreaWords.FarThunder
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    PutridHotbloodedScaffold = {"address": 0x1f, "words": [
        AreaWords.Putrid, AreaWords.HotBlooded, AreaWords.Scaffold
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DetestableGoldenNewTruth = {"address": 0x29, "words": [
        AreaWords.Detestable, AreaWords.Golden, AreaWords.NewTruth
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    BuriedPaganFierySands = {"address": 0x18, "words": [
        AreaWords.Buried, AreaWords.Pagan, AreaWords.FierySands
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    LonelySilentGreatSeal = {"address": 0x19, "words": [
        AreaWords.Lonely, AreaWords.Silent, AreaWords.GreatSeal
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    DetestableGoldenGate = {"address": 0x2a, "words": [
        AreaWords.Detestable, AreaWords.Golden, AreaWords.Gate
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }


class InfectionThetaWordList(WordListBase):
    QuietEternalWhiteDevil = {"address": 0x14, "words": [
        AreaWords.Quiet, AreaWords.Eternal, AreaWords.WhiteDevil
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    SoftSolitaryTriPansy = {"address": 0x21, "words": [
        AreaWords.Soft, AreaWords.Solitary, AreaWords.TriPansy
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    CollapsedMomentarySpiral = {"address": 0x16, "words": [
        AreaWords.Collapsed, AreaWords.Momentary, AreaWords.Spiral
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    BeautifulSomeonesTreasureGem = {"address": 0x22, "words": [
        AreaWords.Beautiful, AreaWords.Someones, AreaWords.TreasureGem
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    CursedDespairedParadise = {"address": 0x17, "words": [
        AreaWords.Cursed, AreaWords.Despaired, AreaWords.Paradise
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    GreatDistantFertileLand = {"address": 0x1a, "words": [
        AreaWords.Great, AreaWords.Distant, AreaWords.FertileLand
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
    ChosenHopelessNothingness = {"address": 0x1b, "words": [
        AreaWords.Chosen, AreaWords.Hopeless, AreaWords.Nothingness
    ],
        "classifications": {1: ItemClassification.progression},
        "volumes": [1]
    }
