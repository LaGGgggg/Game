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
        self.health += self.healing_power

        if self.health > self.max_health:
            self.health = self.max_health

        return self.health

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

            if e == ' `':

                mapp += Fore.LIGHTWHITE_EX + e

            elif e == ' P':

                mapp += Fore.LIGHTGREEN_EX + e

            else:

                mapp += Fore.LIGHTRED_EX + e

        print(mapp + Fore.LIGHTWHITE_EX + ' |')



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

            if e == ' P':

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
            if now_map[player_position[0] - 1][player_position[1] - 1] == ' `':
                correct_directions.append(1)
        except (TypeError, IndexError):
            pass

        # 2
        try:
            if now_map[player_position[0] - 1][player_position[1]] == ' `':
                correct_directions.append(2)
        except (TypeError, IndexError):
            pass

        # 3
        try:
            if now_map[player_position[0] - 1][player_position[1] + 1] == ' `':
                correct_directions.append(3)
        except (TypeError, IndexError):
            pass

        # 4
        try:
            if now_map[player_position[0]][player_position[1] + 1] == ' `':
                correct_directions.append(4)
        except (TypeError, IndexError):
            pass

        # 5
        try:
            if now_map[player_position[0] + 1][player_position[1] + 1] == ' `':
                correct_directions.append(5)
        except (TypeError, IndexError):
            pass

        # 6
        try:
            if now_map[player_position[0] + 1][player_position[1]] == ' `':
                correct_directions.append(6)
        except (TypeError, IndexError):
            pass

        # 7
        try:
            if now_map[player_position[0] + 1][player_position[1] - 1] == ' `':
                correct_directions.append(7)
        except (TypeError, IndexError):
            pass

        # 8
        try:
            if now_map[player_position[0]][player_position[1] - 1] == ' `':
                correct_directions.append(8)
        except (TypeError, IndexError):
            pass

        direction_move = int(input('On why direction you want to move? You can move on ' + str(correct_directions[1:]) +
                                   ' directions and on ' + str(moving_points) + ' cell(s)(or 0 if you want quit)'))

        if direction_move == 0:
            moving = 0
            break

        # Проверка правильности ввода

        while True:
            if direction_move in (correct_directions[0:]):
                break
            print('It`s incorrect value, please enter correct.')
            direction_move = int(input('You can move on ' + str(correct_directions[1:])))

        # Изменение позиции на карте

        now_map[player_position[0]][player_position[1]] = ' `'

        if direction_move == 1:
            now_map[player_position[0] - 1][player_position[1] - 1] = ' P'
            player_position[0] -= 1
            player_position[1] -= 1
        if direction_move == 2:
            now_map[player_position[0] - 1][player_position[1]] = ' P'
            player_position[0] -= 1
        if direction_move == 3:
            now_map[player_position[0] - 1][player_position[1] + 1] = ' P'
            player_position[0] -= 1
            player_position[1] += 1
        if direction_move == 4:
            now_map[player_position[0]][player_position[1] + 1] = ' P'
            player_position[1] += 1
        if direction_move == 5:
            now_map[player_position[0] + 1][player_position[1] + 1] = ' P'
            player_position[0] += 1
            player_position[1] += 1
        if direction_move == 6:
            now_map[player_position[0] + 1][player_position[1]] = ' P'
            player_position[0] += 1
        if direction_move == 7:
            now_map[player_position[0] + 1][player_position[1] - 1] = ' P'
            player_position[0] += 1
            player_position[1] -= 1
        if direction_move == 8:
            now_map[player_position[0]][player_position[1] - 1] = ' P'
            player_position[1] -= 1

        moving_points -= 1

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

    for i in range(len(enemies_dict)):
        if i == 0:
            old_data[16] = 'enemies_list = [[{}, {}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
                                                                                        enemies_dict[i].damage,
                                                                                        enemies_dict[i].ranged_damage,
                                                                                        enemies_dict[i].close_fight_radius,
                                                                                        enemies_dict[i].ranged_combat_radius,
                                                                                        enemies_dict[i].moving_speed,
                                                                                        enemies_dict[i].healing_power,
                                                                                        enemies_dict[i].max_health)
        else:
            old_data[16] = old_data[16][:-2] + ', [{}, {}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
                                                                                              enemies_dict[i].damage,
                                                                                              enemies_dict[i].ranged_damage,
                                                                                              enemies_dict[i].close_fight_radius,
                                                                                              enemies_dict[i].ranged_combat_radius,
                                                                                              enemies_dict[i].moving_speed,
                                                                                              enemies_dict[i].healing_power,
                                                                                              enemies_dict[i].max_health)

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

            if now_map[i][e] != ' `' and now_map[i][e] != ' P' and now_map[i][e] != '#':

                enemies_positions_list.append([i, e])
                enemies_distance[now_map[i][e]] = 0

            if now_map[i][e] == ' P':

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
                enemies_list = enemies_dict_const[difficult]
                for i in range(len(enemies_dict_const[difficult])):
                    enemies_list[i].health = saves.enemies_list[i][0]
                    enemies_list[i].damage = saves.enemies_list[i][1]
                    enemies_list[i].ranged_damage = saves.enemies_list[i][2]
                    enemies_list[i].close_fight_radius = saves.enemies_list[i][3]
                    enemies_list[i].ranged_combat_radius = saves.enemies_list[i][4]
                    enemies_list[i].moving_speed = saves.enemies_list[i][5]
                    enemies_list[i].healing_power = saves.enemies_list[i][6]
                    enemies_list[i].max_health = saves.enemies_list[i][7]
            else:

                difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

                enemies_list = enemies_dict_const[difficult]
        else:
            difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

            enemies_list = enemies_dict_const[difficult]

            now_map = all_maps_const[difficult]

            # Определяем позиции(ю) врагов(а)

            crop_number = round(len(now_map) / 2)

            enemies_number = game_2_0_data.max_map_enemies[difficult]

            while enemies_number != 0:

                for i in range(len(now_map[1:])):

                    if i == 0:
                        i += 1

                    for e in range(len(now_map[i][crop_number:])):
                        if e == 0:
                            e += 1

                        if enemies_number == 0:
                            break

                        enemy_names = []

                        for u in game_2_0_data.enemies_indexes.keys():

                            enemy_names.append(u)

                        choice = ''.join(random.choices(['Go', ''], [1, 99], k=1))

                        if choice == 'Go':

                            choice = ''.join(random.choices(enemy_names, k=1))

                            choice = ' ' + choice[0]

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

                        choice = ''.join(random.choices([' P', ''], [1, 99], k=1))

                        if choice == ' P':

                            player_number -= 1

                            now_map[i][e] = choice

        print('Your map difficult now: ' + difficult)

        map_go = 1

        while map_go == 1:

            # Печать текущей карты

            print('\n')
            print_map()
            map_go = 0

            # Ход игрока

            # Движение

            need_move = input('You need move?(Yes or No(Y/N))')

            if need_move.lower() in ['yes', 'y']:
                player_moving()

            # Использование способностей

            ability_can = ['doing nothing.']

            # Health check

            if player_creature.health < player_creature.max_health:
                ability_can.append('health.')

            # Close fight check

            for items in distance().items():

                if player_creature.close_fight_radius >= items[1]:

                    ability_can.append('"' + items[0][1:] + '" close attack.')

            # Range fight check

            for items in distance().items():

                if player_creature.ranged_combat_radius >= items[1]:

                    ability_can.append('"' + items[0][1:] + '" ranged attack.')

            # циферки на способности и через строку с \n вывод в столбик



            ability = input('What ability you would use? You can use {}'.format(str(ability_can)[1:-1]))

            while ability not in ability_can:

                ability = input('Incorrect value, try again.')

            # Ход врага

        # Автосохранение после конца карты

        end_session(difficult, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated,
                    cells_passed, enemies_list)

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


print('Hello, it`s a nice game, luck don`t help you)')  # Отсыыыылочка

game()
