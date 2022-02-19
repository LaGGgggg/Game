import pdb
import random
import game_2_0_data
import importlib
import random
import math
import os.path
import saves
from colorama import Fore, init

# kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.window import Window


init(autoreset=True)

difficult_list = game_2_0_data.difficult_list
difficult_weights = game_2_0_data.difficult_weights
all_maps_const = game_2_0_data.all_maps


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

    def close_fight(self):

        player_creature.health -= self.damage

        return player_creature.health, self.damage

    def heal(self):

        if self.health > self.max_health:
            self.health = self.max_health
            return self.health, self.max_health

        else:
            self.health += self.healing_power
            return self.health, self.healing_power

    def ranged_combat(self):

        player_creature.health -= self.ranged_damage

        return player_creature.health, self.ranged_damage


Baron = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_1 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_2 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_3 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_4 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_5 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_6 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_7 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_8 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_9 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Baron_10 = EnemyCreature(10, 1, 1, 1, 1, 1, 1, 10)
Elsa = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_1 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_2 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_3 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_4 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_5 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_6 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_7 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_8 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_9 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_10 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Lucius = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_1 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_2 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_3 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_4 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_5 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_6 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_7 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_8 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_9 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_10 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
enemies_dict_const = {"easy": ["Baron"], "medium": ["Elsa"], "hard": ["Elsa", "Baron", "Lucius"]}
enemies_dict_names = {"Baron": Baron, "Baron 1": Baron_1, "Elsa": Elsa, "Elsa 1": Elsa_1, "Elsa 2": Elsa_2, "Elsa 3": Elsa_3, "Elsa 4": Elsa_4, "Elsa 5": Elsa_5, "Elsa 6": Elsa_6, "Elsa 7": Elsa_7, "Elsa 8": Elsa_8, "Elsa 9": Elsa_9, "Elsa 10": Elsa_10, "Baron 2": Baron_2, "Baron 3": Baron_3, "Baron 4": Baron_4, "Baron 5": Baron_5, "Baron 6": Baron_6, "Baron 7": Baron_7, "Baron 8": Baron_8, "Baron 9": Baron_9, "Baron 10": Baron_10, "Lucius": Lucius, "Lucius 1": Lucius_1, "Lucius 2": Lucius_2, "Lucius 3": Lucius_3, "Lucius 4": Lucius_4, "Lucius 5": Lucius_5, "Lucius 6": Lucius_6, "Lucius 7": Lucius_7, "Lucius 8": Lucius_8, "Lucius 9": Lucius_9, "Lucius 10": Lucius_10}


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

    def close_fight(self, creature_name, enemies_dict):

        for i in enemies_dict.values():

            for e in i.items():

                if e[0] == creature_name:

                    e[1].health -= self.damage

                    return e[1].health, self.damage

    def heal(self):

        if self.health > self.max_health:
            self.health = self.max_health
            return self.health, self.max_health

        else:
            self.health += self.healing_power
            return self.health, self.healing_power

    def ranged_combat(self, creature_name, enemies_dict):

        for i in enemies_dict.values():

            for e in i.items():

                if e[0] == creature_name:

                    e[1].health -= self.ranged_damage

                    return e[1].health, self.ranged_damage


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

Window.size = (835, 625)


class CanvasPaintWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        size = Window.size

        with self.canvas:
            Line(points=[0, 0.57 * size[1], size[0], 0.57 * size[1]], width=2)
            Line(points=[0, 0.4 * size[1], size[0], 0.4 * size[1]], width=2)
            Line(points=[0.35 * size[0], 0.4 * size[1], 0.35 * size[0], 0], width=2)


class GameApp(App):

    # map info label

    map_label = Label(text='None', halign='center', valign='middle', size_hint=[.5, .5], pos_hint={'x': .26, 'y': .5},
                      font_size=20)

    # action info label

    action_label = Label(text='None', size_hint=[1, .17], pos_hint={'x': 0, 'y': .4})

    # player info label

    player_info_label = Label(text='None', size_hint=[.35, .4], pos_hint={'x': 0, 'y': 0})

    # enemy info label

    enemy_info_label = Label(text='None', size_hint=[.65, .4], pos_hint={'x': .35, 'y': 0})

    # menu button

    menu_button = Button(text='Click on me.')

    # menu label

    menu_label = Label(text='Hello, it`s a nice game, luck don`t help you)')

    # menu layouts

    menu_finish_layout = AnchorLayout(anchor_x='center', anchor_y='center')

    menu_intermediate_layout = BoxLayout(orientation='vertical', size_hint=[.6, .3])

    def build(self):

        self.menu_button.bind(on_press=self.build_game)

        self.menu_intermediate_layout.add_widget(self.menu_label)

        self.menu_intermediate_layout.add_widget(self.menu_button)

        self.menu_finish_layout.add_widget(self.menu_intermediate_layout)

        return self.menu_finish_layout

    def build_game(self, instance):

        # game layout

        game_layout = FloatLayout()

        # add game widgets

        game_layout.add_widget(self.map_label)

        game_layout.add_widget(self.action_label)

        game_layout.add_widget(self.player_info_label)

        # color -: markup=True, '[color=ffffff]'

        game_layout.add_widget(self.enemy_info_label)

        # Линии разделители между виджетами

        game_layout.add_widget(CanvasPaintWidget())

        # удаляем лишнее и вставляем новое

        self.menu_finish_layout.remove_widget(self.menu_intermediate_layout)

        self.menu_finish_layout.add_widget(game_layout)

        return self.menu_finish_layout


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


#def print_map():
#
#    global now_map
#
#    for i in now_map[1:]:
#
#        n = -1
#        mapp = ''
#
#        for e in i[1:]:
#
#            n += 1
#
#            if n == 0:
#
#                mapp += Fore.LIGHTWHITE_EX + '|'
#
#            if e == '  `':
#
#                mapp += Fore.LIGHTWHITE_EX + e
#
#            elif e == '  P':
#
#                mapp += Fore.LIGHTGREEN_EX + e
#
#            else:
#
#                mapp += Fore.LIGHTRED_EX + e
#
#        print(mapp + Fore.LIGHTWHITE_EX + ' |')
#    print()


def print_map():

    global now_map

    mapp = ''

    for i in now_map[1:]:

        n = -1

        for e in i[1:]:

            n += 1

            if n == 0:
                mapp += '|'

            if e == '  `':

                mapp += e

            elif e == '  P':

                mapp += e

            else:

                mapp += e

        mapp += ' |\n'
    return mapp + '\n'


def enemy_moving(enemy_name, enemy_position=[], player_position=[]):

    global now_map

    # Если нужно, определяем позицию игрока

    if not player_position:

        n1 = 0

        for i in now_map[1:]:

            n1 += 1
            n2 = -1

            for e in i:

                n2 += 1

                if e == '  P':

                    player_position = [n1, n2]

    # Если нужно, определяем позицию врага

    if not enemy_position:

        enemy_number = ''

        for i in enemy_name:

            if i.isnumeric():
                enemy_number += i

        n1 = 0

        for i in now_map[1:]:

            n1 += 1
            n2 = -1

            for e in i:

                n2 += 1

                if e[0] == ' ':
                    if e[1:] == enemy_name[0].upper() + enemy_number:
                        enemy_position = [n1, n2]
                else:
                    if e == enemy_name[0].upper() + enemy_number:
                        enemy_position = [n1, n2]

    # Движение

    # Поиск варианта сближения

    # Делаем сэйв позиции

    enemy_position_save = enemy_position.copy()

    # 1 направление

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] -= 1
        enemy_position[1] -= 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 2

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] -= 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 3

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] -= 1
        enemy_position[1] += 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 4

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[1] += 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 5

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] += 1
        enemy_position[1] += 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 6

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] += 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 7

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[0] += 1
        enemy_position[1] -= 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
        pass

    # 8

    enemy_position = enemy_position_save.copy()

    try:

        enemy_position[1] -= 1

        if now_map[enemy_position[0]][enemy_position[1]] == '  `' and \
            enemy_distance(enemy_name, enemy_position, player_position) < enemy_distance(enemy_name,
                                                                                         enemy_position_save,
                                                                                         player_position):

            now_map[enemy_position_save[0]][enemy_position_save[1]] = '  `'
            now_map[enemy_position[0]][enemy_position[1]] = ' ' + enemy_name[0].upper() + enemy_number
            return enemy_position, player_position

    except (TypeError, IndexError):
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


def enemy_distance(enemy_name, enemy_position=[], player_position=[]):

    global now_map, difficult

    enemy_number = ''

    for i in enemy_name:

        if i.isnumeric():

            enemy_number += i

    for i in range(len(now_map)):

        i += 1

        if enemy_position != [] and player_position != []:
            break

        if i == len(now_map):
            break

        for e in range(len(now_map[i])):

            if not enemy_position:

                if now_map[i][e][0] == ' ':

                    if now_map[i][e][1:] == enemy_name[0].upper() + enemy_number:

                        enemy_position = [i, e]

                else:

                    if now_map[i][e][1:] == enemy_name[0].upper() + enemy_number:

                        enemy_position = [i, e]

            if enemy_position != [] and player_position != []:
                break

            if not player_position:

                if now_map[i][e] == '  P':

                    player_position = [i, e]

            if enemy_position != [] and player_position != []:
                break

    num = math.sqrt((enemy_position[0] - player_position[0]) ** 2 + (enemy_position[1] - player_position[1]) ** 2)

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

        enemy_distance = num
    else:

        enemy_distance = num

    return int(enemy_distance)


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

        if player_creature.health <= 0:
            choose = input(Fore.LIGHTWHITE_EX + 'You want to exit or start again?')

            while choose not in ['exit', 'start again']:
                choose = input(Fore.LIGHTYELLOW_EX + 'Incorrect value!' + Fore.LIGHTWHITE_EX +
                               'You want to "exit" or "start again?"')

            if choose == 'exit':

                game_go = 0
                break

            else:

                # Обнуляем всё до стока

                data = open('saves.py', 'w')

                data.close()

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
                enemies_numbers = {}
                enemy_names = []
                all_choices = []
                numbers_of_enemies = 0

                for u in enemies_dict_const[difficult]:
                    enemy_names.append(u)

                while enemies_number != 0:

                    for i in range(len(now_map[1:])):

                        if i == 0:
                            continue

                        for e in range(len(now_map[i][crop_number:])):
                            if e == 0:
                                continue

                            if enemies_number == 0:
                                break

                            if now_map[i][e] != '  `':
                                continue

                            choice = ''.join(random.choices(['Go', ''], [1, 99], k=1))

                            if choice == 'Go':

                                choice = ''.join(random.choices(enemy_names, k=1))

                                numbers_of_enemies += 1

                                if choice in enemies_numbers.keys():

                                    enemies_numbers[choice] += 1

                                    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                                        choice + ' ' + str(enemies_numbers[choice]): enemies_dict_names[
                                            choice + ' ' + str(enemies_numbers[choice])]}

                                else:

                                    enemies_numbers[choice] = 1

                                    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                                        choice + ' ' + str(enemies_numbers[choice]): enemies_dict_names[
                                            choice + ' ' + str(enemies_numbers[choice])]}

                                c = all_choices.count(choice) + 1

                                all_choices.append(choice)

                                choice = ' ' + choice[0] + str(c)

                                enemies_number -= 1

                                now_map[i][e] = choice

                                ## Смещаем врага если клетка занята

                                #e_1 = 0
                                #i_1 = 0

                                #while now_map[i + i_1][-e + e_1] != '  `':

                                #    direction = ''.join(random.choices(['left', 'right', 'up', 'down'], k=1))

                                #    if direction == 'left':
                                #        e_1 -= 1

                                #    elif direction == 'right':
                                #        e_1 += 1

                                #    elif direction == 'up':
                                #        i_1 -= 1

                                #    elif direction == 'down':
                                #        i_1 += 1

                                #now_map[i + i_1][-e + e_1] = choice

                # Определяем позицию игрока

                player_number = 1

                while player_number != 0:

                    for i in range(len(now_map[1:])):

                        if i == 0:
                            continue

                        for e in range(len(now_map[i][crop_number:])):

                            if e == 0:
                                continue

                            if player_number == 0:
                                break

                            if now_map[i][e] != '  `':
                                continue

                            choice = ''.join(random.choices(['  P', ''], [1, 99], k=1))

                            if choice == '  P':

                                player_number -= 1

                                now_map[i][e] = choice

                                ## Смещаем врага если клетка занята

                                #e_1 = 0
                                #i_1 = 0

                                #while now_map[i + i_1][-e + e_1] != '  `':

                                #    direction = ''.join(random.choices(['left', 'right', 'up', 'down'], k=1))

                                #    if direction == 'left':
                                #        e_1 -= 1

                                #    elif direction == 'right':
                                #        e_1 += 1

                                #    elif direction == 'up':
                                #        i_1 -= 1

                                #    elif direction == 'down':
                                #        i_1 += 1

                                #now_map[i + i_1][e + e_1] = choice
        else:
            difficult = ''.join(random.choices(difficult_list, weights=difficult_weights, k=1))

            now_map = all_maps_const[difficult]

            # Определяем позиции(ю) врагов(а) на карте

            crop_number = round(len(now_map) / 2)

            enemies_number = game_2_0_data.max_map_enemies[difficult]

            enemies_dict = {}
            enemies_numbers = {}
            enemy_names = []
            all_choices = []
            numbers_of_enemies = 0

            for u in enemies_dict_const[difficult]:

                enemy_names.append(u)

            while enemies_number != 0:

                for i in range(len(now_map[1:])):

                    if i == 0:
                        continue

                    for e in range(len(now_map[i][crop_number:])):
                        if e == 0:
                            continue

                        if enemies_number == 0:
                            break

                        if now_map[i][e] != '  `':
                            continue

                        choice = ''.join(random.choices(['Go', ''], [1, 99], k=1))

                        if choice == 'Go':

                            choice = ''.join(random.choices(enemy_names, k=1))

                            numbers_of_enemies += 1

                            if choice in enemies_numbers.keys():

                                enemies_numbers[choice] += 1

                                enemies_dict['Enemy_' + str(numbers_of_enemies)] = {choice + ' ' + str(enemies_numbers[choice]): enemies_dict_names[choice + ' ' + str(enemies_numbers[choice])]}

                            else:

                                enemies_numbers[choice] = 1

                                enemies_dict['Enemy_' + str(numbers_of_enemies)] = {choice + ' ' + str(enemies_numbers[choice]): enemies_dict_names[choice + ' ' + str(enemies_numbers[choice])]}

                            c = all_choices.count(choice) + 1

                            all_choices.append(choice)

                            choice = ' ' + choice[0] + str(c)

                            enemies_number -= 1

                            now_map[i][e] = choice

                            ## Смещаем врага если клетка занята

                            #e_1 = 0
                            #i_1 = 0

                            #while now_map[i + i_1][-e + e_1] != '  `':

                            #    direction = ''.join(random.choices(['left', 'right', 'up', 'down'], k=1))

                            #    if direction == 'left':
                            #        e_1 -= 1

                            #    elif direction == 'right':
                            #        e_1 += 1

                            #    elif direction == 'up':
                            #        i_1 -= 1

                            #    elif direction == 'down':
                            #        i_1 += 1

                            #now_map[i + i_1][-e + e_1] = choice

            # Определяем позицию игрока

            player_number = 1

            while player_number != 0:

                for i in range(len(now_map[1:])):

                    if i == 0:
                        continue

                    for e in range(len(now_map[i][crop_number:])):

                        if e == 0:
                            continue

                        if player_number == 0:
                            break

                        if now_map[i][e] != '  `':
                            continue

                        choice = ''.join(random.choices(['  P', ''], [1, 99], k=1))

                        if choice == '  P':

                            player_number -= 1

                            now_map[i][e] = choice

                            ## Смещаем врага если клетка занята

                            #e_1 = 0
                            #i_1 = 0

                            #while now_map[i + i_1][-e + e_1] != '  `':
                            #
                            #    direction = ''.join(random.choices(['left', 'right', 'up', 'down'], k=1))

                            #    if direction == 'left':
                            #        e_1 -= 1

                            #    elif direction == 'right':
                            #        e_1 += 1

                            #    elif direction == 'up':
                            #        i_1 -= 1

                            #    elif direction == 'down':
                            #        i_1 += 1

                            #now_map[i + i_1][e + e_1] = choice

        print(Fore.LIGHTWHITE_EX + 'Your map difficult now: ' + difficult)

        map_go = 1

        while map_go == 1:

            # Печать текущей карты

            print()
            print_map()

            # Печать характеристик(и) врагов(а)

            enemy_names = []

            for i in enemies_dict.values():

                for e in i.items():

                #for e in i.items():

                #    if e[0] in enemy_names:

                #        n = 1

                #        for u in enemy_names:

                #            if u == e[0]:

                #                n += 1

                #        enemy_names.append(e[0] + ' ' + str(n))

                #        enemy_name = e[0] + ' ' + str(n)

                #    else:

                #        enemy_names.append(e[0])

                #        enemy_name = e[0]

                    print(Fore.LIGHTRED_EX + e[0] + Fore.LIGHTWHITE_EX + ' characters:\nHealth: ' + Fore.LIGHTGREEN_EX +
                          str(e[1].health) + Fore.LIGHTWHITE_EX + '\nHealing power: ' + Fore.LIGHTGREEN_EX +
                          str(e[1].healing_power) + Fore.LIGHTWHITE_EX + '\nClose fight damage: ' + Fore.LIGHTRED_EX +
                          str(e[1].damage) + Fore.LIGHTWHITE_EX + '\nRanged combat damage: ' + Fore.LIGHTRED_EX +
                          str(e[1].ranged_damage) + Fore.LIGHTWHITE_EX + '\nClose fight radius: ' +
                          Fore .LIGHTMAGENTA_EX + str(e[1].close_fight_radius) + Fore.LIGHTWHITE_EX +
                          '\nRanged combat radius: ' + Fore.LIGHTMAGENTA_EX + str(e[1].ranged_combat_radius) +
                          Fore.LIGHTWHITE_EX + '\nMoving speed: ' + Fore.LIGHTCYAN_EX + str(e[1].moving_speed) + '\n')

            # Печать характеристик игрока


            # Ход игрока

            # Движение

            need_move = input(Fore.LIGHTWHITE_EX + 'You need move?(Yes or No(Y/N)(Or "quit" if you want to exit.))')

            if need_move.lower() == 'quit':

                map_go = 0
                game_go = 0
                break

            if need_move.lower() in ['yes', 'y']:
                player_moving()

            # Использование способностей

            ability_can_list = ['doing nothing']
            ability_can_list_colorama = [Fore.LIGHTWHITE_EX + 'Doing nothing']

            # Health check

            if player_creature.health < player_creature.max_health:

                ability_can_list.append('heal')
                ability_can_list_colorama.append(Fore.LIGHTGREEN_EX + 'Heal')

            # Close fight check

            for i in distance().items():

                if player_creature.close_fight_radius >= i[1]:

                    ability_can_list.append('' + i[0][1:].lower() + ' close attack')
                    ability_can_list_colorama.append(Fore.LIGHTWHITE_EX + '' + Fore.LIGHTRED_EX + i[0][1:] +
                                                     Fore.LIGHTWHITE_EX + ' close attack')

            # Range attack check

            for i in distance().items():

                if player_creature.ranged_combat_radius >= i[1]:

                    ability_can_list.append('' + i[0][1:].lower() + ' ranged attack')
                    ability_can_list_colorama.append(Fore.LIGHTWHITE_EX + '' + Fore.LIGHTRED_EX + i[0][1:] +
                                                     Fore.LIGHTWHITE_EX + ' ranged attack')

            # Создаём допустимые номера

            ability_can_str = '\n'
            n = 0

            for i in ability_can_list_colorama:

                n += 1

                ability_can_str += Fore.LIGHTWHITE_EX + str(n) + '. ' + i + '.\n'

            ability_choose = input(Fore.LIGHTWHITE_EX + 'What ability you would use? You can use:' + ability_can_str +
                                   'P.S.: You can write "quit" if want to exit and save your progress.').lower()

            if ability_choose == 'quit':

                map_go = 0
                game_go = 0
                break

            ability_can_numbers = [str(i + 1) for i in range(len(ability_can_list))]

            # Проверка правильности ввода

            while ability_choose not in ability_can_list and ability_choose not in ability_can_numbers:

                ability_choose = input(Fore.LIGHTYELLOW_EX + 'Incorrect value, try again.')

            # Выполнение выбранной способности

            # Ничего не делать

            if 'doing nothing' in ability_choose or ability_choose == '1':

                print(Fore.LIGHTWHITE_EX + 'You didn`t do anything')

            # Лечение

            elif 'heal' in ability_choose or ability_choose == '2' and ability_can_list[1] == 'heal':

                heal_cache = player_creature.heal()

                print(Fore.LIGHTGREEN_EX + 'You' + Fore.LIGHTWHITE_EX + ' health: ' + Fore.LIGHTGREEN_EX + str(heal_cache[0]) + Fore.LIGHTWHITE_EX
                      + '(' + Fore.LIGHTGREEN_EX + '+' + str(heal_cache[1]) + Fore.LIGHTWHITE_EX + ')')

            # Ближняя и дальняя атаки

            elif 'close attack' in ability_choose or ability_choose.isnumeric() and 'close attack' in \
                    ability_can_list[int(ability_choose) - 1] or 'ranged attack' in ability_choose or \
                    ability_choose.isnumeric() and 'ranged attack' in ability_can_list[int(ability_choose) - 1]:

                if ability_choose.isnumeric():

                    ability_choose = ability_can_list[int(ability_choose) - 1]

                enemy_number = ''

                for i in ability_choose[1:]:

                    if i != ' ':

                        enemy_number += i

                    else:

                        break

                for i in enemies_dict.values():

                    for e in i.keys():

                        if e[0] == ability_choose[0].upper() and e[-1] == enemy_number:

                            short_enemy_name = e[0]

                            enemy_name = e

                            break

                if 'close attack' in ability_choose:

                    fight_cache = player_creature.close_fight(enemy_name, enemies_dict)

                else:

                    fight_cache = player_creature.ranged_combat(enemy_name, enemies_dict)

                print(Fore.LIGHTRED_EX + enemy_name + Fore.LIGHTWHITE_EX + ' health: ' + Fore.LIGHTGREEN_EX +
                      str(fight_cache[0]) + Fore.LIGHTWHITE_EX + '(' + Fore.LIGHTRED_EX + '-' +
                      str(fight_cache[1]) + Fore.LIGHTWHITE_EX + ')')

                n = 0

                for i in enemies_dict.values():

                    n += 1

                    for e in i.items():

                        if e[0] == enemy_name:

                            if e[1].health <= 0:

                                print(Fore.LIGHTWHITE_EX + 'You killed ' + Fore.LIGHTRED_EX + e[0] +
                                      Fore.LIGHTWHITE_EX + ', my congratulations')

                                del enemies_dict['Enemy_' + str(n)]

                                n1 = 0

                                for u in now_map:

                                    n1 += 1
                                    n2 = 0

                                    for y in u:

                                        n2 += 1

                                        if len(short_enemy_name + enemy_number) == 2:

                                            if y == ' ' + short_enemy_name + enemy_number:

                                                now_map[n1][n2] = '  `'

                                                break

                                        else:

                                            if y == short_enemy_name + enemy_number:

                                                now_map[n1][n2] = '  `'

                                                break


            #elif 'ranged attack' in ability_choose or ability_choose.isnumeric() and \
            #     'ranged attack' in ability_can_list[int(ability_choose) - 1]:

            #    if ability_choose.isnumeric():

            #        ability_choose = ability_can_list[int(ability_choose) - 1]

            #    enemy_number = ''

            #    for i in ability_choose[1:]:

            #        if i != ' ':

            #            enemy_number += i

            #        else:

            #            break

            #    for i in enemies_dict.values():

            #        for e in i.keys():

            #            if e[0] == ability_choose[0].upper() and e[-1] == enemy_number:

            #                enemy_name = e

            #                break

            #    close_attack_cache = player_creature.ranged_combat(enemy_name, enemies_dict)

            #    print(Fore.LIGHTRED_EX + enemy_name + Fore.LIGHTWHITE_EX + ' health: ' + Fore.LIGHTGREEN_EX +
            #          str(close_attack_cache[0]) + Fore.LIGHTWHITE_EX + '(' + Fore.LIGHTRED_EX + '-' +
            #          str(close_attack_cache[1]) + Fore.LIGHTWHITE_EX + ')')

            # Ход врага

            for i in enemies_dict.values():

                for e in i.items():

                    moving_points = e[1].moving_speed
                    do_points = 1
                    enemy_position = []
                    player_position = []

                    while moving_points != 0:

                        if e[1].damage != 0 and enemy_distance(e[0], enemy_position, player_position) <= \
                                e[1].close_fight_radius:
                            fight_cache = e[1].close_fight()
                            print(Fore.LIGHTRED_EX + e[0] + Fore.LIGHTWHITE_EX + ' close attack you, ' + 'your health: '
                                  + Fore.LIGHTGREEN_EX + str(fight_cache[0]) + Fore.LIGHTWHITE_EX + '(' +
                                  Fore.LIGHTRED_EX + '-' + str(fight_cache[1]) + Fore.LIGHTWHITE_EX + ')')
                            do_points -= 1
                            if player_creature.health <= 0:
                                print(Fore.LIGHTWHITE_EX + 'You died, AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH!')
                                map_go = 0
                            break

                        elif e[1].ranged_damage != 0 and enemy_distance(e[0], enemy_position, player_position) <= \
                                e[1].ranged_combat_radius:
                            fight_cache = e[1].ranged_combat()
                            print(Fore.LIGHTRED_EX + e[0] + Fore.LIGHTWHITE_EX + ' ranged attack you, ' +
                                  'your health: ' + Fore.LIGHTGREEN_EX + str(fight_cache[0]) + Fore.LIGHTWHITE_EX +
                                  '(' + Fore.LIGHTRED_EX + '-' + str(fight_cache[1]) + Fore.LIGHTWHITE_EX + ')')
                            do_points -= 1
                            if player_creature.health <= 0:
                                print(Fore.LIGHTWHITE_EX + 'You died, AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAH!')
                                map_go = 0
                            break

                        else:
                            moving_points -= 1
                            enemy_moving(e[0])

                    if do_points != 0 and e[1].health < e[1].max_health:
                        heal_cache = e[1].heal()
                        print(Fore.LIGHTRED_EX + e[0] + Fore.LIGHTWHITE_EX + ' health: ' + Fore.LIGHTGREEN_EX +
                              str(heal_cache[0]) + Fore.LIGHTWHITE_EX + '(' + Fore.LIGHTGREEN_EX + '+' +
                              str(heal_cache[1]) + Fore.LIGHTWHITE_EX + ')')

                    elif do_points != 0:
                        print(Fore.LIGHTRED_EX + e[0] + Fore.LIGHTWHITE_EX + 'Doing nothing')

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


print(Fore.LIGHTWHITE_EX + 'Hello, it`s a nice game, luck don`t help you)')  # Отсыыыылочка

if __name__ == '__main__':
    GameApp().run()
    game()