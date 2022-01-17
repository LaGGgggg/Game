import random
import game_2_0_data
import game_2_0_functions

difficult_list = game_2_0_data.difficult_list
difficult_weights = game_2_0_data.difficult_weights

the_map_passed = 0
get_artifacts = 0
enemies_killed = 0
damage_received = 0
damage_done = 0
health_regenerated = 0
cells_passed = 0


# Сама игра

print('Hello, it`s a nice game, luck don`t help you)')  # Отсыыыылочка
game_go = 1

while game_go == 1:

    difficult, player_artefacts, player_creature, enemies_dict = game_2_0_functions.start_session()

    if difficult == 'in_hub':

        difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

    print('Your map difficult now: ' + difficult)

    map_go = 1

    while map_go == 1:

        # Дальше надо

        # надо ещё стартовые позиции всех туту сделать !!!!!!!!!!!!!!!!!!!!!!!!

        #

        # надо взять из файла словарь строкой и его в словарь превратить

        # Печать текущей карты

        print('\n')
        game_2_0_functions.print_map(difficult)
        map_go = 0

    # Обнуление характеристик игрока и врагов до стандартных

    game_2_0_functions.player_creature = game_2_0_functions.PlayerCreature(100, 15, 10, 1, 3, 3, 15)

    # тут надо характеристики врагов с ЭТОЙ карты к стоку привести

    # Сохранение всех данных на случай экстренного выключения

    get_artifacts += 1

    get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated, cells_passed = \
        game_2_0_functions.end_session(difficult, str(enemies_dict), get_artifacts, enemies_killed, damage_received,
                                       damage_done, health_regenerated, cells_passed)
    # Статус это название карты или in_hub

    game_go = 0  # убрать потом
