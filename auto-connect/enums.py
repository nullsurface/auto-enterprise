from enum import Enum, Flag, auto


class WPAVersion(Flag):
    WPA1_ENTERPRISE= auto()
    WPA2 = auto()
    WPA3 = auto()


class Dot11w(Enum):
    DISABLED = auto()
    OPTIONAL = auto()
    REQUIRED = auto()


class EAPMethod(Enum):
    PEAP = auto()
    TLS = auto()
