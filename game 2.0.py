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

        data = open('game_2_0_functions.py', 'r', encoding='UTF-8')

        old_data = data.readlines()

        data.close()

        line = max(game_2_0_data.enemies_indexes.values()) + 1

        p = old_data[line][16:-2]

        p3 = []

        p = p.replace('], ', ']&')

        for e in p.split('&'):

            p2 = []
            n = 0

            for i in e.split(': '):
                print(i[0])
                print(i)
                if i[0] == '[':
                    print('-------------------------------')
                    print(i)
                    i = [i[1:-1]]
                    i = str(i).replace("'", '')

                    print(i)
                    print(type(i))
                else:
                    i = i.replace("'", '')
                p2.append(i)

            p3.append(p2)

        p4 = {}

        for i in p3:
            p4[i[0]] = i[1]
        print(p4)
        print(type(p4))

        #p4 = str(str(p4).replace("'", ''))

        old_data[line + 1] = old_data[line + 1][:15] + str(p4) + '\n'

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
