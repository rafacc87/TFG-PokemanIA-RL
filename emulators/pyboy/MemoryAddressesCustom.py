from enum import Enum


class MemoryAddressesCustom(Enum):
    MENU_1 = 0xDFF5
    MENU_2 = 0xDFF9

    BATTLE_OPTION = 0xD05D

    # Missable / Event Flags
    MISSABLE_OBJECTS_FLAGS = 0xD5A6  # Start of missable object flags block (D5A6-D5C5)
    STARTERS_BACK = 0xD5AB
    MEWTWO_FLAG = 0xD5C0  # bit 1: 0=Mewtwo appears, 1=Doesn't

    # Item possession
    HAVE_TOWN_MAP = 0xD5F3
    HAVE_OAKS_PARCEL = 0xD60D

    # Fly / Safari / Fossil Flags
    BIKE_SPEED = 0xD700
    FLY_ANYWHERE_1 = 0xD70B
    FLY_ANYWHERE_2 = 0xD70C
    SAFARI_ZONE_TIME1 = 0xD70D
    SAFARI_ZONE_TIME2 = 0xD70E
    FOSSILIZED_POKEMON = 0xD710

    # World state
    POSITION_IN_AIR = 0xD714
    GOT_LAPRAS = 0xD72E
    DEBUG_NEW_GAME = 0xD732

    # Gym battles
    FOUGHT_GIOVANNI = 0xD751
    FOUGHT_BROCK = 0xD755
    FOUGHT_MISTY = 0xD75E
    FOUGHT_LT_SURGE = 0xD773
    FOUGHT_ERIKA = 0xD77C
    FOUGHT_KOGA = 0xD792
    FOUGHT_BLAINE = 0xD79A
    FOUGHT_SABRINA = 0xD7B3

    # Legendaries
    FOUGHT_ARTICUNO = 0xD782
    FOUGHT_ZAPDOS = 0xD7D4
    FOUGHT_MOLTRES = 0xD7EE
    FOUGHT_MEWTWO = 0xD85F  # bit 2 clear → mewtwo can be caught if D5C0 bit 1 also clear

    # Special encounters
    FOUGHT_SNORLAX_VERMILION = 0xD7D8
    FOUGHT_SNORLAX_CELADON = 0xD7E0

    # SS Anne
    SS_ANNE_PRESENT = 0xD803

    # Safari status
    SAFARI_GAME_OVER = 0xD790  # bit 7 = game over
