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
now_map = all_maps_const

# Сама игра


class EnemyCreature:

    def __init__(self, health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed,
                 healing_power, enemy_difficult):
        self.enemy_difficult = enemy_difficult
        self.health = health
        self.damage = damage
        self.close_fight_radius = close_fight_radius
        self.ranged_combat_radius = ranged_combat_radius
        self.ranged_damage = ranged_damage
        self.moving_speed = moving_speed
        self.healing_power = healing_power

    def close_fight(self, creature):
        creature.health -= self.damage

        return creature.health

    def heal(self):
        self.health += self.healing_power

        return self.health

    def ranged_combat(self, creature):

        creature.health -= self.ranged_damage

        return creature.health


enemy_creature_1 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, "easy")
enemy_creature_2 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, "medium")
enemies_dict_const = {'easy': [enemy_creature_1], 'medium': [enemy_creature_2], "test_map": [enemy_creature_1, enemy_creature_2]}


class PlayerCreature:

    def __init__(self, health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed,
                 healing_power):
        self.health = health
        self.damage = damage
        self.close_fight_radius = close_fight_radius
        self.ranged_combat_radius = ranged_combat_radius
        self.ranged_damage = ranged_damage
        self.moving_speed = moving_speed
        self.healing_power = healing_power

    def close_fight(self, creature):
        creature.health -= self.damage

        return creature.health

    def plus_health(self):
        self.health += self.healing_power

        return self.health

    def ranged_combat(self, creature):
        creature.health -= self.ranged_damage

        return creature.health


player_creature = PlayerCreature(100, 15, 10, 1, 3, 3, 15)


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


def print_map(map_name):

    n = 1

    y = now_map

    try:
        for _ in range(len(now_map)):
            print(Fore.LIGHTWHITE_EX + '|' + ''.join(y[n][1:]) + ' |')

            n += 1
    except:
        TypeError()


def player_moving(map_name, player_position):
    # блок спроса пользователя

    moving = 1

    moving_points = player_creature.moving_speed

    while moving == 1 and moving_points > 0:

        # Обнуление или создание списка корректных направлений

        correct_directions = ['#']

        # Проверка куда можно двигаться

        # 1
        try:
            if now_map[map_name][player_position[0] - 1][player_position[1] - 1] == ' `':
                correct_directions.append(1)
        except:
            IndexError()

        # 2
        try:
            if now_map[map_name][player_position[0] - 1][player_position[1]] == ' `':
                correct_directions.append(2)
        except:
            IndexError()

        # 3
        try:
            if now_map[map_name][player_position[0] - 1][player_position[1] + 1] == ' `':
                correct_directions.append(3)
        except:
            IndexError()

        # 4
        try:
            if now_map[map_name][player_position[0]][player_position[1] + 1] == ' `':
                correct_directions.append(4)
        except:
            IndexError()

        # 5
        try:
            if now_map[map_name][player_position[0] + 1][player_position[1] + 1] == ' `':
                correct_directions.append(5)
        except:
            IndexError()

        # 6
        try:
            if now_map[map_name][player_position[0] + 1][player_position[1]] == ' `':
                correct_directions.append(6)
        except:
            IndexError()

        # 7
        try:
            if now_map[map_name][player_position[0] + 1][player_position[1] - 1] == ' `':
                correct_directions.append(7)
        except:
            IndexError()

        # 8
        try:
            if now_map[map_name][player_position[0]][player_position[1] - 1] == ' `':
                correct_directions.append(8)
        except:
            IndexError()

        direction_move = int(input('On why direction you want to move? You can move on ' + str(correct_directions[1:]) +
                                   ' directions and on ' + str(moving_points) + ' cell(s) or 0 if you want quit'))

        if direction_move == 0:
            moving = 0

        # Проверка правильности ввода

        while True:
            if direction_move in (correct_directions[0:]):
                break
            print('It`s incorrect value, please enter correct.')
            direction_move = int(input('You can move on ' + str(correct_directions[1:])))

        # Изменение позиции на карте

        now_map[map_name][player_position[0]][player_position[1]] = ' `'

        if direction_move == 1:
            now_map[map_name][player_position[0] - 1][player_position[1] - 1] = ' P'
            player_position[0] -= 1
            player_position[1] -= 1
        if direction_move == 2:
            now_map[map_name][player_position[0] - 1][player_position[1]] = ' P'
            player_position[0] -= 1
        if direction_move == 3:
            now_map[map_name][player_position[0] - 1][player_position[1] + 1] = ' P'
            player_position[0] -= 1
            player_position[1] += 1
        if direction_move == 4:
            now_map[map_name][player_position[0]][player_position[1] + 1] = ' P'
            player_position[1] += 1
        if direction_move == 5:
            now_map[map_name][player_position[0] + 1][player_position[1] + 1] = ' P'
            player_position[0] += 1
            player_position[1] += 1
        if direction_move == 6:
            now_map[map_name][player_position[0] + 1][player_position[1]] = ' P'
            player_position[0] += 1
        if direction_move == 7:
            now_map[map_name][player_position[0] + 1][player_position[1] - 1] = ' P'
            player_position[0] += 1
            player_position[1] -= 1
        if direction_move == 8:
            now_map[map_name][player_position[0]][player_position[1] - 1] = ' P'
            player_position[1] -= 1

        moving_points -= 1

        print_map(map_name)

    return player_position


def check_saves():

    if not os.path.exists('saves.py'):
        data = open('saves.py', 'w+')

        data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                   'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                   '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

        n = 17

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

        if len(old_data) != 22 + len(game_2_0_data.difficult_list) or old_data[
                                                                      16:22 + len(game_2_0_data.difficult_list)] \
                != stat_chek:

            data = open('saves.py', 'w+')

            data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                       'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                       '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

            n = 17

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
                enemies_dict, now_map):
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

    old_data[8] = 'player_artefacts = ' + str(player_artefacts.player_artefacts_list) + '\n'  # когда файл перезаписывается через check, то криво записывает

    old_data[12] = 'player_creature = [{}, {}, {}, {}, {}, {}, {}]\n'.format(player_creature.health,
                                                                            player_creature.damage,
                                                                            player_creature.ranged_damage,
                                                                            player_creature.close_fight_radius,
                                                                            player_creature.ranged_combat_radius,
                                                                            player_creature.moving_speed,
                                                                            player_creature.healing_power)
    # Заносим характеристики врага

    for i in range(len(enemies_dict)):
        if i == 0:
            old_data[16] = 'enemies_list = [[{}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
                                                                                    enemies_dict[i].damage,
                                                                                    enemies_dict[i].ranged_damage,
                                                                                    enemies_dict[i].close_fight_radius,
                                                                                    enemies_dict[i].ranged_combat_radius,
                                                                                    enemies_dict[i].moving_speed,
                                                                                    enemies_dict[i].healing_power)
        else:
            old_data[16] = old_data[16][:-2] + ', [{}, {}, {}, {}, {}, {}, {}]]\n'.format(enemies_dict[i].health,
                                                                                         enemies_dict[i].damage,
                                                                                         enemies_dict[i].ranged_damage,
                                                                                         enemies_dict[i].close_fight_radius,
                                                                                         enemies_dict[i].ranged_combat_radius,
                                                                                         enemies_dict[i].moving_speed,
                                                                                         enemies_dict[i].healing_power)

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

        global player_creature, player_artefacts, player_creature, now_map

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
                                                 saves.player_creature[6])
                enemies_list = enemies_dict_const[difficult]
                for i in range(len(enemies_dict_const[difficult])):
                    enemies_list[i].health = saves.enemies_list[i][0]
                    enemies_list[i].damage = saves.enemies_list[i][1]
                    enemies_list[i].ranged_damage = saves.enemies_list[i][2]
                    enemies_list[i].close_fight_radius = saves.enemies_list[i][3]
                    enemies_list[i].ranged_combat_radius = saves.enemies_list[i][4]
                    enemies_list[i].moving_speed = saves.enemies_list[i][5]
                    enemies_list[i].healing_power = saves.enemies_list[i][6]
            else:

                difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

                enemies_list = enemies_dict_const[difficult]
        else:
            difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

            enemies_list = enemies_dict_const[difficult]

            now_map = all_maps_const[difficult]

            # Стартовые позиции здесь

            crop_number = round(len(now_map) / 2)
            print(now_map[1])
            print(len(now_map[1]))
            print(len(now_map[1]) / 2)
            print(round(4.5))
            print(crop_number)
            print()

            enemies_number = game_2_0_data.max_map_enemies[difficult]
            print(enemies_number)

            while enemies_number != 0:
                print('Go')
                print(str(enemies_number) + '  1')

                for i in range(len(now_map[1:])):
                    print(str(enemies_number) + '  2')

                    if i == 0:
                        i += 1
                    print(len(now_map[i][crop_number:]))

                    for e in range(len(now_map[i][crop_number:])):
                        if e == 0:
                            e += 1
                        print(str(enemies_number) + '  3')

                        if enemies_number == 0:
                            break

                        choice = ''.join(random.choices([' E', ''], [1, 99], k=1))

                        if choice == ' E':

                            enemies_number -= 1
                            print('-1')

                            now_map[i][-e] = choice
                    print(str(enemies_number) + '  4')
            print(now_map)

        print('Your map difficult now: ' + difficult)

        map_go = 1

        while map_go == 1:

            # Дальше надо

            # Печать текущей карты

            print('\n')
            print_map(difficult)
            map_go = 0

        # Сохранение всех данных на случай экстренного выключения

        end_session(difficult, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated,
                    cells_passed, enemies_list, now_map)

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
