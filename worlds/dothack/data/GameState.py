from enum import IntFlag


class InfectionGameState(IntFlag):
    TitleScreen = 0x01
    Desktop = 0x02
    Login = 0x03
    LoggingIn = 0x04
    LoggedIn = 0x05
