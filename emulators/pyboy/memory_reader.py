from emulators.pyboy.MemoryAddressesCustom import MemoryAddressesCustom
from emulators.pyboy.memory_addresses import MemoryAddresses


class MemoryReader:
    def __init__(self, emulator):
        self.emulator = emulator
        self.ram = emulator.get_ram_state()

    def _bit_count(self, value):
        return value.bit_count()

    def read_battle_state(self):
        return self.ram[MemoryAddresses.BATTLE_STATE.value]

    def read_fist_pokemon_current_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_second_pokemon_current_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_third_pokemon_current_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_fourth_pokemon_current_hp(self):
        ram = self.emulator.get_ram_state()
        return 256 * self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_fifth_pokemon_current_hp(self):
        ram = self.emulator.get_ram_state()
        return 256 * self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_sixth_pokemon_current_hp(self):
        ram = self.emulator.get_ram_state()
        return 256 * self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_ACTUAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_ACTUAL_HP_2.value] #256 to correct 

    def read_fist_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_TOTAL_HP_2.value] #256 to correct 
    
    def read_second_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_TOTAL_HP_2.value] #256 to correct 
    
    def read_third_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_TOTAL_HP_2.value] #256 to correct 
    
    def read_fourth_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_TOTAL_HP_2.value] #256 to correct 
    
    def read_fifth_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_TOTAL_HP_2.value] #256 to correct 
    
    def read_sixth_pokemon_max_hp(self):
        return 256 * self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_TOTAL_HP_1.value] + self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_TOTAL_HP_2.value] #256 to correct 
    

    def read_player_first_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_LEVEL.value]

    def read_player_second_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_LEVEL.value]

    def read_player_third_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_LEVEL.value]

    def read_player_fourth_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_LEVEL.value]

    def read_player_fifth_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_LEVEL.value]

    def read_player_sixth_pokemon_level(self):
        return self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_LEVEL.value]

    # Opponent
    def read_opponent_first_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_FIRST_POKEMON_LEVEL.value]

    def read_opponent_second_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_SECOND_POKEMON_LEVEL.value]

    def read_opponent_third_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_THIRD_POKEMON_LEVEL.value]

    def read_opponent_fourth_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_FOURTH_POKEMON_LEVEL.value]

    def read_opponent_fifth_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_FIFTH_POKEMON_LEVEL.value]

    def read_opponent_sixth_pokemon_level(self):
        return self.ram[MemoryAddresses.OPPONENT_SIXTH_POKEMON_LEVEL.value]
    
    def read_progress_map(self):
        return self.ram[MemoryAddresses.CURRENT_MAP_NUMBER.value]

    def read_player_current_position(self):
        return (self.ram[MemoryAddresses.CURRENT_PLAYER_POSITION_X.value],self.ram[MemoryAddresses.CURRENT_PLAYER_POSITION_Y.value])
    
    def read_pokemon_in_party(self):
        return self.ram[MemoryAddresses.POKEMON_IN_PARTY.value]
    
    def read_player_first_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_FIRST_POKEMON_NAME.value]
    
    def read_player_second_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_SECOND_POKEMON_NAME.value]

    def read_player_third_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_THIRD_POKEMON_NAME.value]

    def read_player_fourth_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_FOURTH_POKEMON_NAME.value]

    def read_player_fifth_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_FIFTH_POKEMON_NAME.value]

    def read_player_sixth_pokemon_name(self):
        return self.ram[MemoryAddresses.PLAYER_SIXTH_POKEMON_NAME.value]
    
    def read_bagdes_in_possesion(self):
        return self._bit_count(self.ram[MemoryAddresses.BADGES_IN_POSSESION.value]) 

    ## EVENTS
    def read_events_done(self):
        events_done = 0
        for i in range(MemoryAddresses.EVENT_FLAGS_START.value,MemoryAddresses.EVENT_FLAGS_END.value):
            events_done += self._bit_count(self.ram[i])
        return events_done

    def read_event_bits(self):
        return [
            (self.ram[i] >> (7 - j)) & 1  # Extrae cada bit directamente con shift y AND
            for i in range(MemoryAddresses.EVENT_FLAGS_START.value, MemoryAddresses.EVENT_FLAGS_END.value)
            for j in range(8)
        ]

    def get_event_score(self) -> int:
        score = 0

        # Gym leaders
        gym_flags = [
            MemoryAddressesCustom.FOUGHT_BROCK,
            MemoryAddressesCustom.FOUGHT_MISTY,
            MemoryAddressesCustom.FOUGHT_LT_SURGE,
            MemoryAddressesCustom.FOUGHT_ERIKA,
            MemoryAddressesCustom.FOUGHT_KOGA,
            MemoryAddressesCustom.FOUGHT_SABRINA,
            MemoryAddressesCustom.FOUGHT_BLAINE,
            MemoryAddressesCustom.FOUGHT_GIOVANNI,
        ]
        score += sum(1 for addr in gym_flags if self.ram[addr.value] != 0)

        # Legendaries
        for flag in [
            MemoryAddressesCustom.FOUGHT_ARTICUNO,
            MemoryAddressesCustom.FOUGHT_ZAPDOS,
            MemoryAddressesCustom.FOUGHT_MOLTRES,
        ]:
            if self.ram[flag.value] != 0:
                score += 1

        # Mewtwo disponible (No le veo el sentido)
        # if not (self.ram[MemoryAddressesCustom.MEWTWO_FLAG.value] & (1 << 1)):
        #     score += 1

        # Safari
        if self.ram[MemoryAddressesCustom.SAFARI_GAME_OVER.value] & (1 << 7):
            score += 1

        # Objetos clave
        if self.has_town_map():
            score += 1
        if self.has_oaks_parcel():
            score += 1
        if self.ram[MemoryAddressesCustom.BIKE_SPEED.value] > 0:
            score += 1
        if self.ram[MemoryAddressesCustom.FOSSILIZED_POKEMON.value] != 0:
            score += 1
        if self.ram[MemoryAddressesCustom.FLY_ANYWHERE_1.value] != 0:
            score += 1

        # Lugares clave
        if self.ram[MemoryAddressesCustom.SS_ANNE_PRESENT.value] == 1:
            score += 1
        if self.ram[MemoryAddressesCustom.GOT_LAPRAS.value] != 0:
            score += 1
        if self.ram[MemoryAddressesCustom.SAFARI_ZONE_TIME1.value] > 0:
            score += 1

        return score

    def has_town_map(self):
        return self.ram[MemoryAddressesCustom.HAVE_TOWN_MAP.value] != 0

    def has_oaks_parcel(self):
        return self.ram[MemoryAddressesCustom.HAVE_OAKS_PARCEL.value] != 0

    # ----------------------------Helpful functions----------------------------
    def is_in_battle(self):
        return self.read_battle_state() != 0

    def is_menu_open(self):
        """
        Detecta si alguno de los menús del juego está abierto usando combinaciones
        conocidas de valores en las direcciones MENU_1 y MENU_2.
        """
        menu_1 = self.ram[MemoryAddressesCustom.MENU_1.value]
        menu_2 = self.ram[MemoryAddressesCustom.MENU_2.value]

        menu_combinations = {
            (0x80, 0xF5),  # Menú principal
            (0x80, 0x2B),  # Mochila (Items)
            (0x67, 0xBD),  # Pokémon
            (0xA5, 0xC0),  # Jugador
            (0x8D, 0xF0),  # Guardar partida
            (0xE4, 0x07),  # Configuración
        }

        # print(self.debug_menu())  # Para debug visual

        return (menu_1, menu_2) in menu_combinations

    def debug_menu(self):
        menu_1 = self.ram[MemoryAddressesCustom.MENU_1.value]
        menu_2 = self.ram[MemoryAddressesCustom.MENU_2.value]

        menu_map = {
            (0x80, 0xF5): "Menú Principal",
            (0x80, 0x2B): "Mochila (Items)",
            (0x67, 0xBD): "Pokémon",
            (0xA5, 0xC0): "Jugador",
            (0x8D, 0xF0): "Guardar Partida",
            (0xE4, 0x07): "Configuración",
        }

        menu_desc = menu_map.get((menu_1, menu_2), "Ninguno")

        return (
            f" {hex(menu_1)}"
            f" {hex(menu_2)}"
            f" {menu_desc}"
        )

    def is_battle_fight(self):
        return self.ram[MemoryAddressesCustom.BATTLE_OPTION.value] == 0x00

    def is_battle_pokemon(self):
        return self.ram[MemoryAddressesCustom.BATTLE_OPTION.value] == 0x01

    def is_battle_item(self):
        return self.ram[MemoryAddressesCustom.BATTLE_OPTION.value] == 0x02

    def is_battle_run(self):
        return self.ram[MemoryAddressesCustom.BATTLE_OPTION.value] == 0x03

    def get_sum_all_current_hp(self):
        return self.read_fist_pokemon_current_hp() + self.read_second_pokemon_current_hp() + self.read_third_pokemon_current_hp() + self.read_fourth_pokemon_current_hp() + self.read_fifth_pokemon_current_hp() + self.read_sixth_pokemon_current_hp()
    
    def get_sum_all_max_hp(self):
        return self.read_fist_pokemon_max_hp() + self.read_second_pokemon_max_hp() + self.read_third_pokemon_max_hp() + self.read_fourth_pokemon_max_hp() + self.read_fifth_pokemon_max_hp() + self.read_sixth_pokemon_max_hp()
    
    def get_sum_all_player_pokemon_level(self):
        return self.read_player_first_pokemon_level() + self.read_player_second_pokemon_level() + self.read_player_third_pokemon_level() + self.read_player_fourth_pokemon_level() + self.read_player_fifth_pokemon_level() + self.read_player_sixth_pokemon_level()
    
    def get_all_player_pokemon_level(self):
        return [self.read_player_first_pokemon_level(), self.read_player_second_pokemon_level(), self.read_player_third_pokemon_level(), self.read_player_fourth_pokemon_level(), self.read_player_fifth_pokemon_level(), self.read_player_sixth_pokemon_level()]
    
    def get_all_player_pokemon_name(self):
        return [self.read_player_first_pokemon_name(), self.read_player_second_pokemon_name(), self.read_player_third_pokemon_name(), self.read_player_fourth_pokemon_name(), self.read_player_fifth_pokemon_name(), self.read_player_sixth_pokemon_name()]
    
    def get_sum_all_opponent_pokemon_level(self):
        return self.read_opponent_first_pokemon_level() + self.read_opponent_second_pokemon_level() + self.read_opponent_third_pokemon_level() + self.read_opponent_fourth_pokemon_level() + self.read_opponent_fifth_pokemon_level() + self.read_opponent_sixth_pokemon_level()
    
    def get_sum_all_player_normalized_levels(self):
        return self.get_sum_all_player_pokemon_level() / 600 #100 because the maximun level in pokemon is 100
    
    def get_sum_all_opponent_normalized_levels(self):
        return self.get_sum_all_opponent_pokemon_level() / 600 #100 because the maximun level in pokemon is 100
    
    def get_difference_between_events(self):
        return ((MemoryAddresses.EVENT_FLAGS_END.value - MemoryAddresses.EVENT_FLAGS_START.value) * 8)
    
    def get_game_coords(self):
        x, y = self.read_player_current_position()
        map = self.read_progress_map()
        return (x,y,map)

    
