import pdb
import random
import game_2_0_data
import importlib
import random
import math
import os.path
import saves
from colorama import Fore, init

init(autoreset=True)

difficult_list = game_2_0_data.difficult_list
difficult_weights = game_2_0_data.difficult_weights
all_maps_const = game_2_0_data.all_maps

# Сама игра


class EnemyCreature:

    def __init__(self, health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed,
                 healing_power, max_health):
        self.health = health
        self.damage = damage
        self.close_fight_radius = close_fight_radius
        self.ranged_combat_radius = ranged_combat_radius
        self.ranged_damage = ranged_damage
        self.moving_speed = moving_speed
        self.healing_power = healing_power
        self.max_health = max_health

    def close_fight(self, creature):
        creature.health -= self.damage

        return creature.health

    def heal(self):
        self.health += self.healing_power

        if self.health > self.max_health:
            self.health = self.max_health

        return self.health

    def ranged_combat(self, creature):

        creature.health -= self.ranged_damage

        return creature.health


Baron = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Elsa = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
enemies_dict_const = {'easy': [Baron], 'medium': [Elsa]}
enemies_dict_names = {'Baron': Baron, 'Elsa': Elsa}


class PlayerCreature:

    def __init__(self, health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed,
                 healing_power, max_health):
        self.health = health
        self.damage = damage
        self.close_fight_radius = close_fight_radius
        self.ranged_combat_radius = ranged_combat_radius
        self.ranged_damage = ranged_damage
        self.moving_speed = moving_speed
        self.healing_power = healing_power
        self.max_health = max_health

    def close_fight(self, creature):
        creature.health -= self.damage

        return creature.health

    def heal(self):

        if self.health > self.max_health:
            self.health = self.max_health
            return self.health, self.max_health

        else:
            self.health += self.healing_power
            return self.health, self.healing_power

    def ranged_combat(self, creature):
        creature.health -= self.ranged_damage

        return creature.health


player_creature = PlayerCreature(100, 15, 10, 1, 3, 3, 15, 100)


class Artefacts:

    def __init__(self, artefact_do_list, player_artefacts_list):
        self.player_artefacts_list = player_artefacts_list
        self.artefact_do_list = artefact_do_list

    def use_artefact(self, name):
        self.player_artefacts_list[name] -= 1

        for i in self.artefact_do_list[name][1]:

            if i == 'health':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.health += self.artefact_do_list[name][2]

                else:
                    player_creature.health -= self.artefact_do_list[name][2]
            elif i == 'damage':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.damage += self.artefact_do_list[name][2]

                else:
                    player_creature.damage -= self.artefact_do_list[name][2]
            elif i == 'ranged_damage':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.ranged_damage += self.artefact_do_list[name][2]

                else:
                    player_creature.ranged_damage -= self.artefact_do_list[name][2]
            elif i == 'close_fight_radius':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.close_fight_radius += self.artefact_do_list[name][2]

                else:
                    player_creature.close_fight_radius -= self.artefact_do_list[name][2]
            elif i == 'ranged_combat_radius':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.ranged_combat_radius += self.artefact_do_list[name][2]

                else:
                    player_creature.ranged_combat_radius -= self.artefact_do_list[name][2]
            elif i == 'moving_speed':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.moving_speed += self.artefact_do_list[name][2]

                else:
                    player_creature.moving_speed -= self.artefact_do_list[name][2]
            elif i == 'healing_power':
                if self.artefact_do_list[name][0] == '+':
                    player_creature.healing_power += self.artefact_do_list[name][2]

                else:
                    player_creature.healing_power -= self.artefact_do_list[name][2]


player_artefacts = Artefacts(game_2_0_data.artefact_do, game_2_0_data.start_player_artefacts)


def random_artefact(map_name):

    # Открываем и забираем данные из файла

    data = open('game_2_0_data.py', 'r')

    old_data = data.readlines()

    data.close()

    # Берём нужную строку с данными карты по артефактам

    old_data_map_string = old_data[game_2_0_data.map_indexes[map_name]]

    n = 0

    for i in old_data_map_string:
        if i == '{':
            break
        else:
            n += 1

    # Делаем словарь с данными карты

    map_dict_list_1 = str(old_data_map_string[n:])[1:-2].split(', ')

    map_dict_list_2 = []

    for i in map_dict_list_1:
        j = i.split(': ')
        map_dict_list_2.append([str(j[0]).replace("'", ''), int(j[1])])

    map_dict = dict(map_dict_list_2)

    # Рандомим наконец

    artefacts_names_list = list(map_dict.keys())
    weights_list = list(map_dict.values())

    received_artefact = ''.join(random.choices(artefacts_names_list, weights=weights_list, k=1))

    print(Fore.LIGHTWHITE_EX + 'You got ' + str(received_artefact).replace('_', ' '))

    return received_artefact


def print_map():

    global now_map

    for i in now_map[1:]:

        n = -1
        mapp = ''

        for e in i[1:]:

            n += 1

            if n == 0:

                mapp += Fore.LIGHTWHITE_EX + '|'

            if e == '  `':

                mapp += Fore.LIGHTWHITE_EX + e

            elif e == '  P':

                mapp += Fore.LIGHTGREEN_EX + e

            else:

                mapp += Fore.LIGHTRED_EX + e

        print(mapp + Fore.LIGHTWHITE_EX + ' |')
    print()


def enemies_moving():
    pass


def player_moving():

    global now_map

    n1 = 0

    for i in now_map[1:]:

        n1 += 1
        n2 = -1

        for e in i:

            n2 += 1

            if e == '  P':

                player_position = [n1, n2]

    # блок спроса пользователя

    moving = 1

    moving_points = player_creature.moving_speed

    while moving == 1 and moving_points > 0:

        # Обнуление или создание списка корректных направлений

        correct_directions = ['#']

        # Проверка куда можно двигаться

        # 1
        try:
            if now_map[player_position[0] - 1][player_position[1] - 1] == '  `':
                correct_directions.append(1)
        except (TypeError, IndexError):
            pass

        # 2
        try:
            if now_map[player_position[0] - 1][player_position[1]] == '  `':
                correct_directions.append(2)
        except (TypeError, IndexError):
            pass

        # 3
        try:
            if now_map[player_position[0] - 1][player_position[1] + 1] == '  `':
                correct_directions.append(3)
        except (TypeError, IndexError):
            pass

        # 4
        try:
            if now_map[player_position[0]][player_position[1] + 1] == '  `':
                correct_directions.append(4)
        except (TypeError, IndexError):
            pass

        # 5
        try:
            if now_map[player_position[0] + 1][player_position[1] + 1] == '  `':
                correct_directions.append(5)
        except (TypeError, IndexError):
            pass

        # 6
        try:
            if now_map[player_position[0] + 1][player_position[1]] == '  `':
                correct_directions.append(6)
        except (TypeError, IndexError):
            pass

        # 7
        try:
            if now_map[player_position[0] + 1][player_position[1] - 1] == '  `':
                correct_directions.append(7)
        except (TypeError, IndexError):
            pass

        # 8
        try:
            if now_map[player_position[0]][player_position[1] - 1] == '  `':
                correct_directions.append(8)
        except (TypeError, IndexError):
            pass

        direction_move = int(input(Fore.LIGHTWHITE_EX + 'On why direction you want to move? You can move on ' +
                                   str(correct_directions[1:]) + ' directions and on ' + str(moving_points) +
                                   ' cell(s)(or 0 if you want quit)'))

        if direction_move == 0:
            moving = 0
            break

        # Проверка правильности ввода

        while True:
            if direction_move in (correct_directions[0:]):
                break
            print(Fore.LIGHTWHITE_EX + 'It`s incorrect value, please enter correct.')
            direction_move = int(input(Fore.LIGHTWHITE_EX + 'You can move on ' + str(correct_directions[1:])))

        # Изменение позиции на карте

        now_map[player_position[0]][player_position[1]] = '  `'

        if direction_move == 1:
            now_map[player_position[0] - 1][player_position[1] - 1] = '  P'
            player_position[0] -= 1
            player_position[1] -= 1
        if direction_move == 2:
            now_map[player_position[0] - 1][player_position[1]] = '  P'
            player_position[0] -= 1
        if direction_move == 3:
            now_map[player_position[0] - 1][player_position[1] + 1] = '  P'
            player_position[0] -= 1
            player_position[1] += 1
        if direction_move == 4:
            now_map[player_position[0]][player_position[1] + 1] = '  P'
            player_position[1] += 1
        if direction_move == 5:
            now_map[player_position[0] + 1][player_position[1] + 1] = '  P'
            player_position[0] += 1
            player_position[1] += 1
        if direction_move == 6:
            now_map[player_position[0] + 1][player_position[1]] = '  P'
            player_position[0] += 1
        if direction_move == 7:
            now_map[player_position[0] + 1][player_position[1] - 1] = '  P'
            player_position[0] += 1
            player_position[1] -= 1
        if direction_move == 8:
            now_map[player_position[0]][player_position[1] - 1] = '  P'
            player_position[1] -= 1

        moving_points -= 1

        print()
        print_map()


def check_saves():

    if not os.path.exists('saves.py'):
        data = open('saves.py', 'w+')

        data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                   'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                   '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

        n = 20

        for i in game_2_0_data.difficult_list:
            data.write(i + '_passed = 0' + '\n')

            n += 1

        data.write(
            'get_artifacts = 0\nenemies_killed = 0\ndamage_received = 0\ndamage_done = 0\nhealth_regenerated = 0\n'
            'cells_passed = 0\n')

        data.close()

        return False

    else:
        data = open('saves.py', 'r')

        old_data = data.readlines()

        data.close()

        stat_chek = ['get_artifacts = 0\n', 'enemies_killed = 0\n', 'damage_received = 0\n', 'damage_done = 0\n',
                     'health_regenerated = 0\n', 'cells_passed = 0\n']

        n = 0

        for i in game_2_0_data.difficult_list:
            stat_chek.insert(n, i + '_passed = 0' + '\n')

            n += 1

        if len(old_data) != 26 + len(game_2_0_data.difficult_list) or old_data[
                                                                      20:26 + len(game_2_0_data.difficult_list)] \
                != stat_chek:

            data = open('saves.py', 'w+')

            data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                       'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                       '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

            n = 20

            for i in game_2_0_data.difficult_list:
                data.write(i + '_passed = 0' + '\n')

                n += 1

            data.write(
                'get_artifacts = 0\nenemies_killed = 0\ndamage_received = 0\ndamage_done = 0\nhealth_regenerated = 0\n'
                'cells_passed = 0\n')

            data.close()

            return False
        else:
            return True


def end_session(status, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated, cells_passed,
                enemies_dict):

    global player_artefacts, now_map

    # статус это название карты или in_hub

    # сохраняем всё важное(данные игрока, статус игры, данные врагов и статистику

    # Проверка существования файла и его правильности по количеству строк

    importlib.reload(saves)

    check_saves()

    # Открываем и читаем файл

    data = open('saves.py', 'r')

    old_data = data.readlines()

    data.close()

    # Заносим текущий статус

    old_data[0] = 'status = "' + status + '"\n'

    # Заносим карту

    old_data[4] = 'now_map = ' + str(now_map) + '\n'

    # Заносим характеристики игрока

    if type(player_artefacts) == dict:
        p = player_artefacts
    else:
        p = player_artefacts.player_artefacts_list

    old_data[8] = 'player_artefacts = ' + str(p) + '\n'

    old_data[12] = 'player_creature = [{}, {}, {}, {}, {}, {}, {}, {}]\n'.format(player_creature.health,
                                                                                 player_creature.damage,
                                                                                 player_creature.ranged_damage,
                                                                                 player_creature.close_fight_radius,
                                                                                 player_creature.ranged_combat_radius,
                                                                                 player_creature.moving_speed,
                                                                                 player_creature.healing_power,
                                                                                 player_creature.max_health)
    # Заносим характеристики врага

    numbers_of_enemies = 0

    for i in enemies_dict.items():
        for e in i[1].items():

            if numbers_of_enemies == 0:
                numbers_of_enemies += 1
                part_1 = 'enemies_dict = {"Enemy_' + str(numbers_of_enemies) + '": {'
                old_data[16] = part_1 + '"{}": [{}, {}, {}, {}, {}, {}, {}, {}]'.format(e[0], e[1].health, e[1].damage,
                                                                                        e[1].ranged_damage,
                                                                                        e[1].close_fight_radius,
                                                                                        e[1].ranged_combat_radius,
                                                                                        e[1].moving_speed,
                                                                                        e[1].healing_power,
                                                                                        e[1].max_health)
                old_data[16] += '}'
            else:
                numbers_of_enemies += 1
                part_1 = ', "Enemy_' + str(numbers_of_enemies) + '": {'
                old_data[16] += part_1 + '"{}": [{}, {}, {}, {}, {}, {}, {}, {}]'.format(e[0], e[1].health,
                                                                                           e[1].damage,
                                                                                           e[1].ranged_damage,
                                                                                           e[1].close_fight_radius,
                                                                                           e[1].ranged_combat_radius,
                                                                                           e[1].moving_speed,
                                                                                           e[1].healing_power,
                                                                                           e[1].max_health)
                old_data[16] += '}'
    old_data[16] += '}\n'

        #if i == 0:
        #    old_data[16] = 'enemies_list = [[{}, {}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
        #                                                                                enemies_dict[i].damage,
        #                                                                                enemies_dict[i].ranged_damage,
        #                                                                                enemies_dict[i].close_fight_radius,
        #                                                                                enemies_dict[i].ranged_combat_radius,
        #                                                                                enemies_dict[i].moving_speed,
        #                                                                                enemies_dict[i].healing_power,
        #                                                                                enemies_dict[i].max_health)
        #else:
        #    old_data[16] = old_data[16][:-2] + ', [{}, {}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
        #                                                                                      enemies_dict[i].damage,
        #                                                                                      enemies_dict[i].ranged_damage,
        #                                                                                      enemies_dict[i].close_fight_radius,
        #                                                                                      enemies_dict[i].ranged_combat_radius,
        #                                                                                      enemies_dict[i].moving_speed,
        #                                                                                      enemies_dict[i].healing_power,
        #                                                                                      enemies_dict[i].max_health)

    # Заносим статистику

    n = 20

    importlib.reload(saves)

    for i in game_2_0_data.difficult_list:

        k = old_data[n][len(i) + 10:-1]

        old_data[n] = i + '_passed = ' + str(k) + '\n'

        n += 1

    old_data[n] = 'get_artifacts = ' + str(saves.get_artifacts + get_artifacts) + '\n'
    n += 1
    old_data[n] = 'enemies_killed = ' + str(saves.enemies_killed + enemies_killed) + '\n'
    n += 1
    old_data[n] = 'damage_received = ' + str(saves.damage_received + damage_received) + '\n'
    n += 1
    old_data[n] = 'damage_done = ' + str(saves.damage_done + damage_done) + '\n'
    n += 1
    old_data[n] = 'health_regenerated = ' + str(saves.health_regenerated + health_regenerated) + '\n'
    n += 1
    old_data[n] = 'cells_passed = ' + str(saves.cells_passed + cells_passed) + '\n'

    # Записываем всё в файл

    new_data = open('saves.py', 'w')

    for i in old_data:

        new_data.write(str(i))

    new_data.close()


def distance():

    global now_map, difficult

    enemies_positions_list = []
    player_position = []
    enemies_distance = {}

    for i in range(len(now_map)):

        if len(enemies_positions_list) == game_2_0_data.max_map_enemies[difficult] and player_position != []:
            break

        if i == len(now_map):
            break

        i += 1

        for e in range(len(now_map[i])):

            if now_map[i][e] != '  `' and now_map[i][e] != '  P' and now_map[i][e] != '#':

                enemies_positions_list.append([i, e])
                enemies_distance[now_map[i][e]] = 0

            if now_map[i][e] == '  P':

                player_position = [i, e]

            if len(enemies_positions_list) == game_2_0_data.max_map_enemies[difficult] and player_position != []:

                break

    n = -1

    for i in enemies_distance.keys():

        n += 1

        num = math.sqrt((enemies_positions_list[n][0] - player_position[0]) ** 2 +
                        (enemies_positions_list[n][1] - player_position[1]) ** 2)
        if '.0' not in str(num):
            y = 0
            crop_str_num_1 = ''
            crop_str_num_2 = ''
            for e in str(num):
                if y == 1:
                    crop_str_num_2 = int(e)
                    break
                if e != '.':
                    crop_str_num_1 += e
                else:
                    y += 1
            if int(crop_str_num_2) > 4:
                num = int(crop_str_num_1[0]) + 1
            else:
                num = int(crop_str_num_1[0])
            enemies_distance[i] = num
        else:
            enemies_distance[i] = num

    return enemies_distance


def game():

    importlib.reload(game_2_0_data)

    the_map_passed = {}
    for i in game_2_0_data.difficult_list:
        the_map_passed[i] = 0
    get_artifacts = 0
    enemies_killed = 0
    damage_received = 0
    damage_done = 0
    health_regenerated = 0
    cells_passed = 0

    game_go = 1

    while game_go == 1:

        global player_creature, player_artefacts, player_creature, now_map, difficult

        # Проверка saves

        if check_saves():

            # импорт данных из saves

            difficult = saves.status
            player_artefacts = saves.player_artefacts
            now_map = saves.now_map

            if difficult != 'in_hub':
                player_creature = PlayerCreature(saves.player_creature[0], saves.player_creature[1],
                                                 saves.player_creature[2], saves.player_creature[3],
                                                 saves.player_creature[4], saves.player_creature[5],
                                                 saves.player_creature[6], saves.player_creature[7])
                enemies_dict = {'Enemy_1': {}}
                number_of_enemy = 0
                for i in saves.enemies_dict.values():
                    number_of_enemy += 1
                    for e in i.keys():
                        enemies_dict['Enemy_' + str(number_of_enemy)] = {}
                        enemies_dict['Enemy_' + str(number_of_enemy)][e] = enemies_dict_names[e]
                for i in saves.enemies_dict.items():
                    for e in i[1].items():
                        enemies_dict[i[0]][e[0]].health = e[1][0]
                        enemies_dict[i[0]][e[0]].damage = e[1][1]
                        enemies_dict[i[0]][e[0]].ranged_damage = e[1][2]
                        enemies_dict[i[0]][e[0]].close_fight_radius = e[1][3]
                        enemies_dict[i[0]][e[0]].ranged_combat_radius = e[1][4]
                        enemies_dict[i[0]][e[0]].moving_speed = e[1][5]
                        enemies_dict[i[0]][e[0]].healing_power = e[1][6]
                        enemies_dict[i[0]][e[0]].max_health = e[1][7]
            else:

                difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

                now_map = all_maps_const[difficult]

                # Определяем позиции(ю) врагов(а) на карте

                crop_number = round(len(now_map) / 2)

                enemies_number = game_2_0_data.max_map_enemies[difficult]

                enemies_dict = {}
                enemy_names = []
                all_choices = []
                numbers_of_enemies = 0

                for u in game_2_0_data.enemies_indexes.keys():
                    enemy_names.append(u)

                while enemies_number != 0:

                    for i in range(len(now_map[1:])):

                        if i == 0:
                            i += 1

                        for e in range(len(now_map[i][crop_number:])):
                            if e == 0:
                                continue

                            if enemies_number == 0:
                                break

                            choice = ''.join(random.choices(['Go', ''], [1, 99], k=1))

                            if choice == 'Go':

                                choice = ''.join(random.choices(enemy_names, k=1))

                                numbers_of_enemies += 1

                                enemies_dict['Enemy_' + str(numbers_of_enemies)] = {choice: enemies_dict_names[choice]}

                                if choice in all_choices:

                                    c = all_choices.count(choice) + 1

                                    all_choices.append(choice)

                                    choice = ' ' + choice[0] + str(c)

                                else:

                                    all_choices.append(choice)

                                    choice = '  ' + choice[0]

                                enemies_number -= 1

                                now_map[i][-e] = choice

                # Определяем позицию игрока

                player_number = 1

                while player_number != 0:

                    for i in range(len(now_map[1:])):

                        if i == 0:
                            i += 1

                        for e in range(len(now_map[i][crop_number:])):

                            if e == 0:
                                e += 1

                            if player_number == 0:
                                break

                            choice = ''.join(random.choices(['  P', ''], [1, 99], k=1))

                            if choice == '  P':
                                player_number -= 1

                                now_map[i][e] = choice
        else:
            difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

            now_map = all_maps_const[difficult]

            # Определяем позиции(ю) врагов(а) на карте

            crop_number = round(len(now_map) / 2)

            enemies_number = game_2_0_data.max_map_enemies[difficult]

            enemies_dict = {}
            enemy_names = []
            all_choices = []
            numbers_of_enemies = 0

            for u in game_2_0_data.enemies_indexes.keys():

                enemy_names.append(u)

            while enemies_number != 0:

                for i in range(len(now_map[1:])):

                    if i == 0:
                        i += 1

                    for e in range(len(now_map[i][crop_number:])):
                        if e == 0:
                            continue

                        if enemies_number == 0:
                            break

                        choice = ''.join(random.choices(['Go', ''], [1, 99], k=1))

                        if choice == 'Go':

                            choice = ''.join(random.choices(enemy_names, k=1))

                            numbers_of_enemies += 1

                            enemies_dict['Enemy_' + str(numbers_of_enemies)] = {choice: enemies_dict_names[choice]}

                            if choice in all_choices:

                                c = all_choices.count(choice) + 1

                                all_choices.append(choice)

                                choice = ' ' + choice[0] + str(c)

                            else:

                                all_choices.append(choice)

                                choice = '  ' + choice[0]

                            enemies_number -= 1

                            now_map[i][-e] = choice

            # Определяем позицию игрока

            player_number = 1

            while player_number != 0:

                for i in range(len(now_map[1:])):

                    if i == 0:
                        i += 1

                    for e in range(len(now_map[i][crop_number:])):

                        if e == 0:
                            e += 1

                        if player_number == 0:
                            break

                        choice = ''.join(random.choices(['  P', ''], [1, 99], k=1))

                        if choice == '  P':

                            player_number -= 1

                            now_map[i][e] = choice

        print(Fore.LIGHTWHITE_EX + 'Your map difficult now: ' + difficult)

        map_go = 1

        while map_go == 1:

            # Печать текущей карты

            print()
            print_map()
            map_go = 0

            # Печать характеристик(и) врагов(а)

            enemy_names = []

            for i in enemies_dict.values():

                for e in i.items():

                    if e[0] in enemy_names:

                        n = 1

                        for u in enemy_names:

                            if u == e[0]:

                                n += 1

                        enemy_names.append(e[0] + ' ' + str(n))

                        enemy_name = e[0] + ' ' + str(n)

                    else:

                        enemy_names.append(e[0])

                        enemy_name = e[0]

                    print(Fore.LIGHTWHITE_EX + enemy_name + ' characters:\nHealth ' + Fore.LIGHTGREEN_EX +
                          str(e[1].health) + Fore.LIGHTWHITE_EX +
                          '\nHealing power ' + Fore.LIGHTGREEN_EX + str(e[1].healing_power) + Fore.LIGHTWHITE_EX +
                          '\nClose fight damage ' + Fore.LIGHTRED_EX + str(e[1].damage) +
                          Fore.LIGHTWHITE_EX +
                          '\nRanged combat damage ' + Fore.LIGHTRED_EX + str(e[1].ranged_damage) + Fore.LIGHTWHITE_EX +
                          '\nClose fight radius ' + Fore .LIGHTMAGENTA_EX + str(e[1].close_fight_radius) +
                          Fore.LIGHTWHITE_EX +
                          '\nRanged combat radius ' + Fore.LIGHTMAGENTA_EX + str(e[1].ranged_combat_radius) +
                          Fore.LIGHTWHITE_EX +
                          '\nMoving speed ' +
                          Fore.LIGHTCYAN_EX + str(e[1].moving_speed) + '\n')

            # Ход игрока

            # Движение

            need_move = input(Fore.LIGHTWHITE_EX + 'You need move?(Yes or No(Y/N))')

            if need_move.lower() in ['yes', 'y']:
                player_moving()

            # Использование способностей

            player_creature.health = 9

            ability_can_list = ['doing nothing']
            ability_can_list_colorama = [Fore.LIGHTWHITE_EX + 'Doing nothing']

            # Health check

            if player_creature.health < player_creature.max_health:

                ability_can_list.append('heal')
                ability_can_list_colorama.append(Fore.LIGHTWHITE_EX + 'Heal')

            # Close fight check

            for items in distance().items():

                if player_creature.close_fight_radius >= items[1]:

                    ability_can_list.append('' + items[0][1:].lower() + ' close attack')
                    ability_can_list_colorama.append(Fore.LIGHTWHITE_EX + '' + Fore.LIGHTRED_EX + items[0][1:] +
                                                     Fore.LIGHTWHITE_EX + ' close attack')

            # Range fight check

            for items in distance().items():

                if player_creature.ranged_combat_radius >= items[1]:

                    ability_can_list.append('' + items[0][1:].lower() + ' ranged attack')
                    ability_can_list_colorama.append(Fore.LIGHTWHITE_EX + '' + Fore.LIGHTRED_EX + items[0][1:] +
                                                     Fore.LIGHTWHITE_EX + ' ranged attack')

            ability_can_str = '\n'
            n = 0

            for i in ability_can_list_colorama:

                n += 1

                ability_can_str += Fore.LIGHTWHITE_EX + str(n) + '. ' + i + '.\n'

            ability_choose = input(Fore.LIGHTWHITE_EX + 'What ability you would use? You can use:' + ability_can_str).\
                lower()

            ability_can_numbers = [str(i + 1) for i in range(len(ability_can_list))]

            while ability_choose not in ability_can_list and ability_choose not in ability_can_numbers:

                ability_choose = input(Fore.LIGHTYELLOW_EX + 'Incorrect value, try again.')

            if 'doing nothing' in ability_choose or ability_choose == '1':

                print(Fore.LIGHTWHITE_EX + 'you didn`t do anything')

            elif 'heal' in ability_choose or ability_choose == '2' and ability_can_list[1] == 'heal':

                heal_cache = player_creature.heal()

                print(Fore.LIGHTWHITE_EX + 'You health: ' + Fore.LIGHTGREEN_EX + str(heal_cache[0]) + Fore.LIGHTWHITE_EX
                      + '(' + Fore.LIGHTGREEN_EX + '+' + str(heal_cache[1]) + Fore.LIGHTWHITE_EX + ')')

            elif 'close attack' in ability_choose or 'close attack' in ability_can_list[int(ability_choose)]:
                # чекнуть
                enemy_names_cache = {}

                for i in enemies_dict.values():

                    for e in list(i.keys()):

                        if e in list(enemy_names_cache.values()):

                            enemy_names_cache[e] = 0

                        else:

                            enemy_names_cache[e] = 0

                ability_choose_number = ''

                for i in ability_choose[1:]:  # 1 or 0?

                    if i != ' ':
                        ability_choose_number += i
                    else:
                        break

                enemy_names_cache_str_list = []
                k = -1

                for i in enemy_names_cache.items():

                    if i[0][0] == ability_choose[0].upper():

                        for e in enemies_dict.values():

                            k += 1

                            for u in e.items():

                                for o in list(enemy_names_cache.keys()):

                                    enemy_names_cache_str_list.append(str(o))

                                if u[0] == enemy_names_cache_str_list[k]:

                                    if i[1] == ability_choose_number:

                                        player_creature.close_fight(u[1])

                                    else:
                                        print(i)

                                        # Тут всё ок, надо просто код ниже от сюда<:

                                        #i[1] += 1
                                        #enemy_names_cache[j] += 1

                                        # До сюда>

                                        

            # Ход врага

        # Автосохранение после конца карты

        end_session(difficult, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated,
                    cells_passed, enemies_dict)

        # Сброс локальной статистики

        the_map_passed = {}
        for i in game_2_0_data.difficult_list:
            the_map_passed[i] = 0
        get_artifacts = 0
        enemies_killed = 0
        damage_received = 0
        damage_done = 0
        health_regenerated = 0
        cells_passed = 0

        game_go = 0  # убрать потом


print(Fore.LIGHTWHITE_EX + 'Hello, it`s a nice game, luck don`t help you)')  # Отсыыыылочка

game()
