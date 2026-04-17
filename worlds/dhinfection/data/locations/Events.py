from enum import IntEnum, auto, Enum


class InfectionEventBase(Enum):
    @classmethod
    def from_address(self, address: int):
        for member in self:
            if member.value["address"] == address:
                return member
        return None


class InfectionStoryEvents(InfectionEventBase):
    FirstDataBug = {"address": 0xa44f39, "bits": 0b00000100}
    LearnGateHacking = {"address": 0xa44f52, "bits": 0b00000010}
    SavedPiros = {"address": 0xa44f41, "bits": 0b00000001}
    BoardProtected = {"address": 0xa44f5a, "bits": 0b00010000}
    BlackRoseDungeon = {"address": 0xa44f6a, "bits": 0b00000100}
    ElkMiaFavorite = {"address": 0xa44f71, "bits": 0b10000000}
    PirosDiary = {"address": 0xa44f7b, "bits": 0b00100000}
    MistralMeetUp = {"address": 0xa44f90, "bits": 0b00000001}
    Epitaph00 = {"address": 0xa44f92, "bits": 0b00000001}
    DescendentsOfFianna = {"address": 0xa44fa8, "bits": 0b00000001}
    EpitaphQ = {"address": 0xa44fb0, "bits": 0b00000001}
    MetMeg = {"address": 0xa44fb8, "bits": 0b00000001}


class CompletionConditions(InfectionEventBase):
    SkeithDefeated = {"address": 0xa44fc0, "bits": 0b00000001}
    ParasiteDragonDefeated = {"address": 0xa450b8, "bits": 0b00010000}


class InfectionGoldenGoblins(InfectionEventBase):
    Stehony = {"address": 0xa45059, "bits": 0b00000001}
    Jonue = {"address": 0xa45061, "bits": 0b00000001}
    Zyan = {"address": 0xa45069, "bits": 0b00000001}
    Albert = {"address": 0xa45071, "bits": 0b00000001}
    Martina = {"address": 0xa45079, "bits": 0b00000001}


class InfectionOptionalPartyMembers(InfectionEventBase):
    Sanjuro = {"address": 0xa45099, "bits": 0b00000001}
    Gardenia = {"address": 0xa450a2, "bits": 0b00000100}
    Natsume = {"address": 0xa450b0, "bits": 0b10000000}
    GracefulBook = {"address": 0xa450a9, "bits": 0b00000001}
