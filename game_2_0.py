import game_2_0_data
import importlib
import random
import math
import os.path
import saves
from colorama import Fore, init

# kivy

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Line
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty


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

kv = '''

<ScrollViewLabel>:
    Label:
        text: root.text
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width - 15, None
        markup: True

<MenuScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .6
            Label:
                text: 'Hello, it`s a nice game, luck don`t help you:).'
            Button:
                text: 'Game.'
                on_release: root.manager.current = 'game'
            Button:
                text: 'Customizer.'
                on_release: root.manager.current = 'customizer'
            Button:
                text: 'Settings.'
                on_release: root.manager.current = 'settings'

<GameScreen>:
    FloatLayout:
        id: game_layout_1
        canvas:
            Line:
                points: 0.35 * self.width, self.height, 0.35 * self.width, 0
                width: 2
            Line:
                points: 0.35 * self.width, 0.57 * self.height, self.width, 0.57 * self.height
                width: 2
            Line:
                points: 0.35 * self.width, 0.4 * self.height, self.width, 0.4 * self.height
                width: 2
            Line:
                points: 0.73 * self.width, 0.4 * self.height, 0.73 * self.width, 0
                width: 2
        Label:
            id: game_label_1
            text: 'Map text'
            size_hint: .65, .43
            pos_hint: {'x': .35, 'y': .57}
            font_size: 18
            markup: True
            font_name: 'font1.ttf'
        ScrollViewLabel:
            id: game_label_2
            size_hint: .5, .17
            pos_hint: {'x': .35, 'y': .4}
            font_size: 15
            text: 'Action label:\\n\\nDo you want to play?'

        GridLayout:
            id: game_layout_2
            cols: 3
            pos_hint: {'x': .85, 'y': .41}
            size_hint: .15, .15
            Button:
                id: game_layout_2_button_1
                text: 'yes'
                on_release: root.build_game()
            Button:
                id: game_layout_2_button_2
                text: 'no'
                on_release: root.manager.current = 'menu'

        Label:
            id: game_label_3
            text: 'Player characters info label'
            size_hint: .38, .4
            font_size: 14
            pos_hint: {'x': .35, 'y': 0}
            markup: True
            text_size: self.width - 15, self.height - 10
            valign: 'top'
            halign: 'left'
        Label:
            id: game_label_4
            text: 'Player artefact info layout'
            size_hint: .27, .4
            font_size: 14
            pos_hint: {'x': .73, 'y': 0}
            markup: True
            text_size: self.width - 15, self.height - 10
            valign: 'top'
            halign: 'left'
        ScrollViewLabel:
            id: game_label_5
            text: 'Enemy info label'
            font_size: 14
            size_hint: .347, 1
            pos_hint: {'x': 0, 'y': 0}

<CustomizerScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .3
            Label:
                text: 'Don`t work now.'
            Button:
                text: 'Back to menu'
                on_release: root.manager.current = 'menu'

<SettingsScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .3
            Label:
                text: 'Don`t work now'
            Button:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'

'''

Builder.load_string(kv)


class ScrollViewLabel(ScrollView):
    text = StringProperty('')

class MenuScreen(Screen):
    pass


class GameScreen(Screen):

    def print_map(self):

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

                    mapp += '[color=00ff00]' + e + '[/color]'

                else:

                    mapp += '[color=ff0000]' + e + '[/color]'

            mapp += ' |\n'

        self.ids['game_label_1'].text = mapp

    def build_game(self):

        self.ids['game_layout_2'].remove_widget(self.ids['game_layout_2_button_1'])
        self.ids['game_layout_2'].remove_widget(self.ids['game_layout_2_button_2'])

        global player_creature, player_artefacts, player_creature, now_map, difficult

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

        self.ids['game_label_2'].text += '\nYour map difficult now: ' + difficult

        # Печать текущей карты

        self.print_map()

        # Печать характеристик(и) врагов(а)

        enemy_names = []  # ?

        self.ids['game_label_5'].text = ''

        for i in enemies_dict.values():

            for e in i.items():

                self.ids['game_label_5'].text += '[color=ff0000][size=16]' + e[0] +\
                                                '[/color] characters:[/size]\nHealth: [color=00ff00]' +\
                                                str(e[1].health) + '[/color]\nHealing power: [color=00ff00]' +\
                                                str(e[1].healing_power) +\
                                                '[/color]\nClose fight damage: [color=ff0000]' + str(e[1].damage) +\
                                                '[/color]\nRanged combat damage: [color=ff0000]' +\
                                                str(e[1].ranged_damage) +\
                                                '[/color]\nClose fight radius: [color=ff00ff]' +\
                                                str(e[1].close_fight_radius) +\
                                                '[/color]\nRanged combat radius: [color=ff00ff]' +\
                                                str(e[1].ranged_combat_radius) +\
                                                '[/color]\nMoving speed: [color=00ffff]' + str(e[1].moving_speed) +\
                                                '[/color]\n\n'

        # Вывод характеристик игрока

        self.ids['game_label_3'].text = '[size=16]You characters:[/size]\nHealth: [color=00ff00]' +\
                                        str(player_creature.health) + '[/color]\nHealing power: [color=00ff00]' +\
                                        str(player_creature.healing_power) +\
                                        '[/color]\nClose fight damage: [color=ff0000]' + str(player_creature.damage) +\
                                        '[/color]\nRanged combat damage: [color=ff0000]' +\
                                        str(player_creature.ranged_damage) +\
                                        '[/color]\nClose fight radius: [color=ff00ff]' +\
                                        str(player_creature.close_fight_radius) +\
                                        '[/color]\nRanged combat radius: [color=ff00ff]' +\
                                        str(player_creature.ranged_combat_radius) +\
                                        '[/color]\nMoving speed: [color=00ffff]' + str(player_creature.moving_speed) +\
                                        '[/color]'

        n = 0

        for i in player_artefacts.player_artefacts_list.items():

            if i[1] != 0:

                n += 1

                k = -1

                for e in i[0]:

                    if e in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

                        break

                    k += 1

                self.ids['game_label_4'].text = '[size=16]You artefacts:\n[/size]' + i[0].replace('_', ' ')[:k] + \
                                                '[font=font4.ttf]' + i[0].replace('_', ' ')[k:] + ': [/font]' +\
                                                str(i[1])

        if n == 0:
            self.ids['game_label_4'].text = 'You don`t have any artefacts:(.'


class CustomizerScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class GameApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(CustomizerScreen(name='customizer'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


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


if __name__ == '__main__':
    GameApp().run()
