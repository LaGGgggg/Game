import importlib
import game_2_0_data


def made_map(map_difficult, map_weight, lines, cells_in_line, map_artefacts_list, map_artefacts_chances,
             map_enemies_list, max_enemies_on_map):

    importlib.reload(game_2_0_data)

    n = 1
    all_y = [i for i in range(101)]  # карта до ста строк

    for _ in range(int(lines)):
        all_y[n] = [' `' for _ in range(0, int(cells_in_line) + 1)]
        all_y[n].insert(0, '#')
        n += 1

    for i in all_y:

        if type(i) == int:
            if n == 0:
                n += 1
            else:
                break

    # открываем, читаем и записываем файл

    data = open('game_2_0_data.py', 'r')

    old_data = data.readlines()

    data.close()

    # вытягиваем нужные данные и изменяем ка нужно

    if old_data[0][17:] == '[]\n':
        old_data[0] = old_data[0][:-2] + '"' + map_difficult + '"]\n'
    else:
        old_data[0] = old_data[0][:-2] + ', "' + map_difficult + '"]\n'

    if old_data[1][17:] == '[]\n':
        old_data[1] = old_data[1][:-2] + str(map_weight) + ']\n'
    else:
        old_data[1] = old_data[1][:-2] + ', ' + str(map_weight) + ']\n'

    if old_data[2][17:] == '{}\n':
        old_data[2] = old_data[2][:-2] + '"' + map_difficult + '": ' + str(all_y) + '}\n'
    else:
        old_data[2] = old_data[2][:-2] + ', "' + map_difficult + '": ' + str(all_y) + '}\n'

    # Добавление артефактов к карте

    new_map_index = str(max(game_2_0_data.map_indexes.values()) + 1)

    if old_data[4] == 'map_indexes = {}':
        old_data[4] = old_data[4][:-2] + '"' + map_difficult + '": ' + new_map_index + '}\n'
    else:
        old_data[4] = old_data[4][:-2] + ', "' + map_difficult + '": ' + new_map_index + '}\n'

    new_map_index = int(new_map_index)

    old_data.append('\n')

    old_data[new_map_index] = map_difficult + '_map_artefact_chances = {'

    for i in range(len(map_artefacts_list)):

        if i != 0:

            old_data[new_map_index] = old_data[new_map_index] + ', "' + map_artefacts_list[i] + '": ' + \
                                      str(map_artefacts_chances[i])
        else:
            old_data[new_map_index] = old_data[new_map_index] + '"' + map_artefacts_list[i] + '": ' + \
                                      str(map_artefacts_chances[i])

    old_data[new_map_index] = old_data[new_map_index] + '}\n'

    p = game_2_0_data.max_map_enemies
    p[map_difficult] = max_enemies_on_map

    old_data[10] = old_data[10][:19] + str(p)[1:] + '\n'

    # Записываем всё в файл

    data = open('game_2_0_data.py', 'w')

    for i in old_data:

        data.write(i)

    data.close()

    data = open('game 2.0.py', 'r', encoding='UTF-8')

    old_data = data.readlines()

    data.close()

    # Добавляем новую карту с её врагами

    line = max(game_2_0_data.enemies_indexes.values()) + 1

    p = ''
    n = 0

    for i in map_enemies_list:

        p += str(i)

        if n != 0 or i == map_enemies_list[-1]:

            n += 1

        else:

            p += ', '

    old_data[line] = old_data[line][:-2] + ', "' + map_difficult + '": [' + p + ']}\n'

    data = open('game 2.0.py', 'w', encoding='UTF-8')

    for i in old_data:

        data.write(i)

    data.close()


def made_enemy(health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed, healing_power,
               enemy_difficult, enemy_name):

    reformat_specifications = '{}, {}, {}, {}, {}, {}, {}'.format(health, damage, ranged_damage, close_fight_radius,
                                                                  ranged_combat_radius, moving_speed, healing_power)

    importlib.reload(game_2_0_data)

    # изменяем кол-во врагов:

    # открываем и читаем

    data = open('game_2_0_data.py', 'r')

    old_data = data.readlines()

    data.close()

    # узнаём новый индекс врага

    line = max(game_2_0_data.enemies_indexes.values())

    # добавляем новый индекс для нового врага

    old_data[5] = old_data[5][:-2] + ', "' + enemy_name + '": ' + str(line + 1) + '}\n'

    # записываем нужные данные

    data = open('game_2_0_data.py', 'w')

    for i in old_data:

        data.write(i)

    data.close()

    # читаем файл

    data = open('game 2.0.py', 'r', encoding='UTF-8')

    old_data = data.readlines()

    data.close()

    # добавляем нового врага

    old_data[line] = old_data[line] + enemy_name + ' = EnemyCreature(' + reformat_specifications + ')\n'

    # добавляем врага к нужной карте

    p = old_data[line + 1][22:-2]

    p3 = []

    p = p.replace('], ', ']&')

    for e in p.split('&'):

        p2 = []
        n = 0

        for i in e.split(': '):
            if n == 1:
                p2.append(i[:-1] + ', ' + enemy_name + ']')

            else:
                p2.append(i)

            if i[1:-1] == enemy_difficult:
                n = 1

        p3.append(p2)

    p4 = {}

    for i in p3:
        p4[i[0]] = i[1]

    p4 = str(str(p4).replace("'", ''))

    old_data[line + 1] = old_data[line + 1][:21] + str(p4) + '\n'

    # Добавляем врага в enemies_dict_names

    if old_data[line + 2] == 'enemies_dict_names = {}\n':

        old_data[line + 2] = old_data[line + 2][:-2] + '"' + enemy_name + '": ' + enemy_name + '}\n'

    else:

        old_data[line + 2] = old_data[line + 2][:-2] + ', "' + enemy_name + '": ' + enemy_name + '}\n'

    # Записываем всё в файл

    data = open('game 2.0.py', 'w', encoding='UTF-8')

    for i in old_data:

        data.write(i)

    data.close()


def made_artefact(name, plus_or_minus, how_many_do, how_many_on_start, artefact_chance, artefact_map, what_do):
    # what_do списком

    importlib.reload(game_2_0_data)

    # открываем, читаем и записываем файл

    data = open('game_2_0_data.py', 'r')

    old_data = data.readlines()

    data.close()

    # добавляем :

    if old_data[7][25:] == '{}\n':
        old_data[7] = old_data[7][:-2] + '"' + name + '": ' + str(how_many_on_start) + '}\n'

    else:
        old_data[7] = old_data[7][:-2] + ', "' + name + '": ' + str(how_many_on_start) + '}\n'

    if old_data[8][14:] == '{}\n':
        old_data[8] = old_data[8][:-2] + '"' + name + '": ["' + plus_or_minus + '", ' + str(what_do) + ', ' + \
                    str(how_many_do) + ']}\n'

    else:
        old_data[8] = old_data[8][:-2] + ', "' + name + '": ["' + plus_or_minus + '", ' + str(what_do) + ', ' \
                       + str(how_many_do) + ']}\n'

    line = game_2_0_data.map_indexes[artefact_map]

    if old_data[line] == artefact_map + '_map_artefact_chances = {}\n':
        old_data[line] = old_data[line][:-2] + '"' + name + '": ' + str(artefact_chance) + '}\n'

    else:
        old_data[line] = old_data[line][:-2] + ', "' + name + '": ' + str(artefact_chance) + '}\n'

    # записываем нужные данные

    data = open('game_2_0_data.py', 'w')

    for i in old_data:
        data.write(i)

    data.close()


def change_maps():
    pass


def change_enemies():
    pass


def change_artefacts():
    pass


def change_player():
    pass


print('Hello, this is customizer for game 2.0')
