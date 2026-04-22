from dataclasses import dataclass
from typing import List, Dict, Any
from .Addresses import VolumeAddresses, InfectionAddresses, MutationAddresses, OutbreakAddresses, QuarantineAddresses


@dataclass
class VolumeData:
    volume: int
    addresses: VolumeAddresses
    event_locations: List[Any] = None
    wordlist_locations: List[Any] = None
    party_member_items: List[Any] = None
    server_items: List[Any] = None
    wordlist_items: List[Any] = None


VOLUME_DATA: Dict[int, VolumeData] = {
    1: VolumeData(volume=1, addresses=InfectionAddresses),
    2: VolumeData(volume=2, addresses=MutationAddresses),
    3: VolumeData(volume=3, addresses=OutbreakAddresses),
    4: VolumeData(volume=4, addresses=QuarantineAddresses),
}
