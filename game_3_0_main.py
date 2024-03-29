import game_3_0_data
import importlib
import copy
import math
from os import path, remove
import random

# kivy

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

difficult_list = copy.deepcopy(game_3_0_data.difficult_list)
difficult_weights = copy.deepcopy(game_3_0_data.difficult_weights)
all_maps_const = copy.deepcopy(game_3_0_data.all_maps)

number_of_save = game_3_0_data.number_of_save


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

        if type(player_artefacts) == dict:

            p = copy.deepcopy(game_3_0_data.artefact_do)

        else:

            p = self.artefact_do_list

        for i in p[name][1]:

            if i == 'health':
                if p[name][0] == '+':
                    player_creature.health += p[name][2]
                    player_creature.max_health += p[name][2]

                else:
                    player_creature.health -= p[name][2]
            elif i == 'damage':
                if p[name][0] == '+':
                    player_creature.damage += p[name][2]

                else:
                    player_creature.damage -= p[name][2]
            elif i == 'ranged_damage':
                if p[name][0] == '+':
                    player_creature.ranged_damage += p[name][2]

                else:
                    player_creature.ranged_damage -= p[name][2]
            elif i == 'close_fight_radius':
                if p[name][0] == '+':
                    player_creature.close_fight_radius += p[name][2]

                else:
                    player_creature.close_fight_radius -= p[name][2]
            elif i == 'ranged_combat_radius':
                if p[name][0] == '+':
                    player_creature.ranged_combat_radius += p[name][2]

                else:
                    player_creature.ranged_combat_radius -= p[name][2]
            elif i == 'moving_speed':
                if p[name][0] == '+':
                    player_creature.moving_speed += p[name][2]

                else:
                    player_creature.moving_speed -= p[name][2]
            elif i == 'healing_power':
                if p[name][0] == '+':
                    player_creature.healing_power += p[name][2]

                else:
                    player_creature.healing_power -= p[name][2]


player_artefacts = Artefacts(game_3_0_data.artefact_do, game_3_0_data.start_player_artefacts)

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
                on_release: root.manager.current = 'save_choose'
            Button:
                text: 'Customizer.'
                on_release: root.manager.current = 'customizer'
            Button:
                text: 'Settings.'
                on_release: root.manager.current = 'settings'
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Quit.'
            on_release: app.get_running_app().stop()
<SaveChooseScreen>:
    on_pre_enter: root.build()
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .6
            Label:
                text: 'Choose current save or create new.'
            Button:
                id: save_choose_button_1
                text: 'None'
                on_release: 
                    root.manager.current = 'game'
                    root.manager.screens[1].new_save('save_1.py')
            Button:
                id: save_choose_button_2
                text: 'None'
                on_release: 
                    root.manager.current = 'game'
                    root.manager.screens[1].new_save('save_2.py')
            Button:
                id: save_choose_button_3
                text: 'None'
                on_release: 
                    root.manager.current = 'game'
                    root.manager.screens[1].new_save('save_3.py')
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Back to menu.'
            on_release: root.manager.current = 'menu'
<GameScreen>:
    FloatLayout:
        id: game_layout_1
        canvas:
            Line:
                points: 0.31 * self.width, self.height, 0.31 * self.width, 0
                width: 2
            Line:
                points: 0.31 * self.width, 0.57 * self.height, self.width, 0.57 * self.height
                width: 2
            Line:
                points: 0.585 * self.width, 0.4 * self.height, self.width, 0.4 * self.height
                width: 2
            Line:
                points: 0.585 * self.width, 0.57 * self.height, 0.585 * self.width, 0
                width: 2
            Line:
                points: 0.745 * self.width, 0.57 * self.height, 0.745 * self.width, 0.4 * self.height
                width: 2
        Label:
            id: game_label_1
            text: 'Map label'
            size_hint: .69, .43
            pos_hint: {'x': .31, 'y': .57}
            font_size: 18
            markup: True
            font_name: 'font1.ttf'
        ScrollViewLabel:
            id: game_label_2
            size_hint: .27, .55
            pos_hint: {'x': .31, 'y': .014}
            font_size: 15
            text: ''

        # player choose layout(move direction and ability choose)

        GridLayout:
            id: game_layout_2
            cols: 3
            pos_hint: {'x': .59, 'y': .41}
            size_hint: .15, .15
            Button:
                id: game_layout_2_button_1
                text: 'Yes'
                on_release: root.build_game('')
            Button:
                id: game_layout_2_button_2
                text: 'No'
                on_release: root.manager.current = 'menu'
        FloatLayout:
            id: game_extra_layout_1
            Button:
                pos_hint: {'x': 15, 'y': 15}
                id: game_layout_3_button_1
                text: 'Inventory.'
                on_release: 
                    root.ids['game_label_3'].size_hint = (0, 0)
                    root.ids['game_label_4'].size_hint = (.415, .4)
                    root.ids['game_layout_3'].remove_widget(root.ids['game_layout_3_button_1'])
                    root.ids['game_extra_layout_1'].add_widget(root.ids['game_layout_3_button_1'])
                    root.ids['game_extra_layout_1'].remove_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_layout_3'].add_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_layout_4'].pos_hint = {'x': .845, 'y': .237}
            Button:
                pos_hint: {'x': 15, 'y': 15}
                id: game_layout_3_button_2
                text: 'Characters.'
                on_release:
                    root.ids['game_label_3'].size_hint = (.415, .4)
                    root.ids['game_label_4'].size_hint = (0, 0)
                    root.ids['game_extra_layout_1'].remove_widget(root.ids['game_layout_3_button_1'])
                    root.ids['game_layout_3'].add_widget(root.ids['game_layout_3_button_1'])
                    root.ids['game_layout_3'].remove_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_extra_layout_1'].add_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_layout_4'].pos_hint = {'x': 15, 'y': 15}
        GridLayout:
            id: game_layout_3
            rows: 1
            orientation: 'rl-tb'
            pos_hint: {'x': .751, 'y': .41}
            size_hint: .247, .15
            Button:
                id: game_layout_3_button_4
                text: 'Quit.'
                on_release: root.manager.current = 'menu'
            Button:
                id: game_layout_3_button_5
                text: 'Inventory.'
                on_release:
                    root.ids['game_extra_layout_1'].remove_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_layout_3'].add_widget(root.ids['game_layout_3_button_2'])
                    root.ids['game_layout_3'].remove_widget(root.ids['game_layout_3_button_5'])
                    root.ids['game_label_3'].size_hint = (0, 0)
                    root.ids['game_label_4'].size_hint = (.415, .4)
                    root.ids['game_layout_4'].pos_hint = {'x': .845, 'y': .237}
        Label:
            id: game_label_3
            text: 'Player characters info label'
            size_hint: .415, .4
            font_size: 14
            pos_hint: {'x': .585, 'y': 0}
            markup: True
            text_size: self.width - 15, self.height - 10
            valign: 'top'
            halign: 'left'
        Label:
            id: game_label_4
            text: 'Player artefact info label'
            size_hint: 0, 0
            font_size: 14
            pos_hint: {'x': .585, 'y': 0}
            markup: True
            text_size: self.width - 15, self.height - 10
            valign: 'top'
            halign: 'left'
        GridLayout:
            id: game_layout_4
            cols: 3
            size_hint: .15, .15
            pos_hint: {'x': 15, 'y': 15}
            Button:
                text: '+'
                on_release: root.ids['game_layout_4_label_1'].text = str(int(root.ids['game_layout_4_label_1'].text) + 1)
            Label:
                id: game_layout_4_label_1
                text: '1'
            Button:
                text: '-'
                on_release: root.ids['game_layout_4_label_1'].text = str(int(root.ids['game_layout_4_label_1'].text) - 1)
            Button:
                text: 'Upload.'
                on_release: root.use_artefact()
        ScrollViewLabel:
            id: game_label_5
            text: 'Enemy characters info label'
            font_size: 14
            size_hint: .306, 1
            pos_hint: {'x': 0, 'y': 0}
<CustomizerScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .6
            Label:
                text: 'Hello, it`s customizer for this game.\\nWhat you want to do?'
            Button:
                text: 'Add map.'
                on_release: root.manager.current = 'add_map'
            Button:
                text: 'Add enemy.'
                on_release: root.manager.current = 'add_enemy'
            Button:
                text: 'Add artefact.'
                on_release: root.manager.current = 'add_artefact'
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Back to menu'
            on_release: root.manager.current = 'menu'
<AddMapScreen>:
    on_pre_enter: root.build()
    GridLayout:
        size_hint: .8, 1
        cols: 3
        Label:
        Label:
            id: add_map_label_0
            text: 'Enter map characters please.'
            halign: 'center'
            markup: True
            font_size: 17
        Label:
        Label:
            id: add_map_label_1
            size_hint: .8, .2
            text: 'Map name:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_1
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'No numbers, all lowercase,\\n not symbols "/" and "&".' 
        Label:
            id: add_map_label_2
            size_hint: .8, .2
            text: 'Map chance:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_2
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            font_size: 13
            text: 'One number\\n(start map chance to drop for player).'
        Label:
            id: add_map_label_3
            size_hint: .8, .2
            text: 'Lines in map:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_3
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_map_label_4
            size_hint: .8, .2
            text: 'Cells in line:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_4
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_map_label_5
            size_hint: .8, .2
            text: 'Map artefacts:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_5
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            id: add_map_extra_label_1
            halign: 'center'
            font_size: 13
            markup: True
            text: 'Any from this list\\n(with comma-separated enumeration):\\n'
        Label:
            id: add_map_label_6
            size_hint: .8, .2
            text: 'Map artefacts chances:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_6
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number on one artefact.'
            font_size: 13
        Label:
            id: add_map_label_7
            size_hint: .8, .2
            text: 'Map enemies names:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_7
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            id: add_map_extra_label_2
            halign: 'center'
            font_size: 13
            markup: True
            text: 'Any from this list\\n(with comma-separated enumeration):\\n'
        Label:
            id: add_map_label_8
            size_hint: .8, .2
            text: 'Max enemies on map:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_map_text_input_8
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number'
        Label:
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        Button:
            size_hint: .2, .12
            text: 'Apply.'
            on_release: root.check()
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Back to menu.'
            on_release: root.manager.current = 'menu'
<AddEnemyScreen>:
    on_pre_enter: root.build()
    GridLayout:
        size_hint: .8, 1
        cols: 3
        Label:
        Label:
            id: add_enemy_label_0
            markup: True
            text: 'Enter enemy characters please.'
            halign: 'center'
        Label:
        Label:
            id: add_enemy_label_1
            size_hint: .8, .2
            text: 'Health:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_1
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.' 
        Label:
            id: add_enemy_label_2
            size_hint: .8, .2
            text: 'Damage:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_2
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            text: 'One number.'
        Label:
            id: add_enemy_label_3
            size_hint: .8, .2
            text: 'Ranged attack damage:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_3
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_enemy_label_4
            size_hint: .8, .2
            text: 'Close fight radius:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_4
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_enemy_label_5
            size_hint: .8, .2
            text: 'Ranged combat radius:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_5
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_enemy_label_6
            size_hint: .8, .2
            text: 'Moving speed:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_6
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            markup: True
            text: 'One number.\\n[size=11](How many cells enemy can go per turn).[/size]'
            halign: 'center'
        Label:
            id: add_enemy_label_7
            size_hint: .8, .2
            text: 'Healing power:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_7
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            markup: True
            text: 'One number.\\n[size=11](How many health enemy can heal per turn).[/size]'
            halign: 'center'
        Label:
            id: add_enemy_label_8
            size_hint: .8, .2
            text: 'Max health:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_8
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            markup: True
            text: 'One number.\\n[size=10](Enemy can start with not full health(1 input), but\\n can`t have health more then their max health.)[/size]'
            halign: 'center'
        Label:
            id: add_enemy_label_9
            size_hint: .8, .2
            text: 'Enemy maps:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_9
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            id: add_enemy_extra_label_1
            halign: 'center'
            font_size: 13
            markup: True
            text: 'Any from this list(all lowercase and\\nwith comma-separated enumeration):\\n'
        Label:
            id: add_enemy_label_10
            size_hint: .8, .2
            text: 'Enemy name:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_enemy_text_input_10
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'No numbers,\\nall except first letter lowercase,\\nnot symbols "/" and "&".'
        Label:
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        Button:
            size_hint: .2, .12
            text: 'Apply.'
            on_release: root.check()
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Back to menu.'
            on_release: root.manager.current = 'menu'
<AddArtefactScreen>:
    on_pre_enter: root.build()
    GridLayout:
        size_hint: .8, 1
        cols: 3
        Label:
        Label:
            id: add_artefact_label_0
            markup: True
            text: 'Enter artefact characters please.'
            halign: 'center'
        Label:
        Label:
            id: add_artefact_label_1
            size_hint: .8, .2
            text: 'Name:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_1
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            text: 'No numbers,\\nall except first letter lowercase,\\nnot symbols "/" and "&".' 
        Label:
            id: add_artefact_label_2
            size_hint: .8, .2
            text: 'Baff or debaff:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_2
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            text: '"+" or "-".'
        Label:
            id: add_artefact_label_3
            size_hint: .8, .2
            text: 'Artefact power:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_3
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            text: 'One number.\\n(How many characters + or -).'
        Label:
            id: add_artefact_label_4
            size_hint: .8, .2
            text: 'How many on start:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_4
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            text: 'One number.\\n(How many player have on start).'
        Label:
            id: add_artefact_label_5
            size_hint: .8, .2
            text: 'Artefact chance:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_5
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            text: 'One number.'
        Label:
            id: add_artefact_label_6
            size_hint: .8, .2
            text: 'Artefact map:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_6
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            id: add_artefact_extra_label_1
            halign: 'center'
            font_size: 13
            markup: True
            text: 'Any from this list(all lowercase and\\nwith comma-separated enumeration):\\n'
        Label:
            id: add_artefact_label_7
            size_hint: .8, .2
            text: 'Artefact characters:'
        TextInput:
            background_color: (0.51, 0.51, 0.55, 1)
            id: add_artefact_text_input_7
            text: ''
            size_hint: .7, .2
            multiline: False
        Label:
            halign: 'center'
            font_size: 13
            markup: True
            text: 'Any from this list(all lowercase and\\nwith comma-separated enumeration):\\n[size=11][u]health[/u], [u]damage[/u], [u]ranged damage[/u],\\n[u]close fight radius[/u], [u]ranged combat radius[/u],\\n[u]moving speed[/u], [u]healing power[/u], [u]max health[/u][/size].'
        Label:
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        Button:
            size_hint: .2, .12
            text: 'Apply.'
            on_release: root.check()
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        Button:
            size_hint: .14, .07
            text: 'Back to menu.'
            on_release: root.manager.current = 'menu'
<SettingsScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .6, .3
            Label:
                halign: 'center'
                text: 'You can`t configure anything.\\nRemember, it`s a hard game.'
            Button:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
<StatisticScreen>:
    on_pre_enter: root.build()
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        Label:
            size_hint: .7, .8
            id: statistic_label_1
            text: ''
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        Button:
            size_hint: .3, .2
            text: 'Go to menu'
            on_release: root.manager.current = 'menu'
'''


class ScrollViewLabel(ScrollView):
    text = StringProperty('')


class MenuScreen(Screen):
    pass


class SaveChooseScreen(Screen):

    def build(self):

        global saves_list

        saves_list = []

        if path.exists('save_1.py'):
            saves_list.append('save_1.py')
            self.ids['save_choose_button_1'].text = 'Save 1'
        if path.exists('save_2.py'):
            saves_list.append('save_2.py')
            self.ids['save_choose_button_2'].text = 'Save 2'
        if path.exists('save_3.py'):
            saves_list.append('save_3.py')
            self.ids['save_choose_button_3'].text = 'Save 3'


class GameScreen(Screen):

    moving_points = ''

    current_save = ''

    def print_player_characters(self):

        self.ids['game_label_3'].text = '[size=16]You characters:[/size]\nHealth: [color=00ff00]' + \
                                        str(player_creature.health) + '[/color]\nHealing power: [color=00ff00]' + \
                                        str(player_creature.healing_power) + \
                                        '[/color]\nClose fight damage: [color=ff0000]' + str(player_creature.damage) + \
                                        '[/color]\nRanged combat damage: [color=ff0000]' + \
                                        str(player_creature.ranged_damage) + \
                                        '[/color]\nClose fight radius: [color=ff00ff]' + \
                                        str(player_creature.close_fight_radius) + \
                                        '[/color]\nRanged combat radius: [color=ff00ff]' + \
                                        str(player_creature.ranged_combat_radius) + \
                                        '[/color]\nMoving speed: [color=00ffff]' + str(player_creature.moving_speed) + \
                                        '[/color]'

    def print_artefacts(self):

        if type(player_artefacts) == dict:

            p = player_artefacts

        else:

            p = player_artefacts.player_artefacts_list

        n = 0

        self.ids['game_label_4'].text = '[size=16]You artefacts:[/size]'

        for i in p.items():

            if i[1] != 0:

                n += 1

                k = -1

                for e in i[0]:

                    if e in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        break

                    k += 1

                self.ids['game_label_4'].text += '\n' + i[0].replace('_', ' ')[:k] + '[font=font4.ttf]' + \
                                                 i[0].replace('_', ' ')[k:] + ': [/font]' + str(i[1])

        if n == 0:
            self.ids['game_label_4'].text = 'You don`t have any artefacts:(.'

    def print_enemies_characters(self):

        self.ids['game_label_5'].text = ''

        for i in enemies_dict.values():

            for e in i.items():

                if e[1].health > 0:
                    self.ids['game_label_5'].text += '[color=ff0000][size=16]' + e[0] + \
                                                     '[/color] characters:[/size]\nHealth: [color=00ff00]' + \
                                                     str(e[1].health) + '[/color]\nHealing power: [color=00ff00]' + \
                                                     str(e[1].healing_power) + \
                                                     '[/color]\nClose fight damage: [color=ff0000]' + str(e[1].damage) + \
                                                     '[/color]\nRanged combat damage: [color=ff0000]' + \
                                                     str(e[1].ranged_damage) + \
                                                     '[/color]\nClose fight radius: [color=ff00ff]' + \
                                                     str(e[1].close_fight_radius) + \
                                                     '[/color]\nRanged combat radius: [color=ff00ff]' + \
                                                     str(e[1].ranged_combat_radius) + \
                                                     '[/color]\nMoving speed: [color=00ffff]' + str(e[1].moving_speed) + \
                                                     '[/color]\n\n'

    def use_artefact(self):

        if difficult == 'in_hub':

            self.ids['game_label_2'].text += '\nTEST YOUR [color=ff00ff]LUCK[/color]!!!'

            return

        global player_artefacts

        if type(player_artefacts) == dict:

            p = player_artefacts

        else:

            p = player_artefacts.player_artefacts_list

        n = 0

        number_of_artefact = int(self.ids['game_layout_4_label_1'].text)

        for i in p.items():

            if i[1] != 0:

                n += 1

                if n == number_of_artefact:

                    if type(player_artefacts) == dict:

                        Artefacts.use_artefact(self, i[0])

                        player_artefacts[i[0]] -= 1

                    else:

                        player_artefacts.use_artefact(i[0])

                        player_artefacts.player_artefacts_list[i[0]] -= 1

                    self.print_artefacts()

                    self.print_player_characters()

                    self.ids['game_label_2'].text += '\nYou use ' + i[0].replace('_', ' ')[:len(i[0]) - 1] + \
                                                     '[font=font4.ttf]' + i[0][len(i[0]) - 1:] + '[/font]'

                    break

    def label_6_plus(self, instance):

        global game_layout_2_label_6

        game_layout_2_label_6.text = str(int(game_layout_2_label_6.text) + 1)

    def label_6_minus(self, instance):

        global game_layout_2_label_6

        game_layout_2_label_6.text = str(int(game_layout_2_label_6.text) - 1)

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

    def go_menu_now(self, instance):

        sm.current = 'menu'

    def go_menu(self, instance):

        # go to menu

        global sm

        sm.current = 'menu'

        # clear game_screen

        self.ids['game_label_1'].text = 'Map label'
        self.ids['game_label_2'].text = 'Action label:'
        self.ids['game_label_3'].text = 'Player characters info label'
        self.ids['game_label_4'].text = 'Player artefact info layout'
        self.ids['game_label_5'].text = 'Enemy characters info label'

        self.ids['game_layout_2'].clear_widgets()

        game_layout_button_1 = Button(text='Yes', on_release=self.build_game)
        game_layout_button_2 = Button(text='No', on_release=self.go_menu_now)

        self.ids['game_layout_2'].add_widget(game_layout_button_1)
        self.ids['game_layout_2'].add_widget(game_layout_button_2)

    def go_statistic(self, instance):

        # go to statistic screen

        global sm

        sm.current = 'statistic'

        # prepare game_screen to the next game

        self.ids['game_label_1'].text = 'Map label'
        self.ids['game_label_2'].text = 'Action label:'
        self.ids['game_label_3'].text = 'Player characters info label'
        self.ids['game_label_4'].text = 'Player artefact info layout'
        self.ids['game_label_5'].text = 'Enemy characters info label'

        self.ids['game_layout_2'].clear_widgets()

        game_layout_button_1 = Button(text='Yes', on_release=self.build_game)
        game_layout_button_2 = Button(text='No', on_release=self.go_menu_now)

        self.ids['game_layout_2'].add_widget(game_layout_button_1)
        self.ids['game_layout_2'].add_widget(game_layout_button_2)

    def new_save(self, instance):

        global saves_list, saves_list, sm

        if instance in saves_list:

            self.ids['game_label_2'].text = ''

            self.current_save = instance

            return self.build_game(instance)

        else:

            self.ids['game_label_2'].text = 'Action label:\n\nDo you want to play?'

            saves_list.append(instance)

            self.current_save = instance

    def new_turn(self):

        # Движение

        self.ids['game_label_2'].text += '\nYou need move?'

        game_layout_2_button_3 = Button(text='Yes', on_release=self.player_moving_part_1)
        game_layout_2_button_4 = Button(text='No', on_release=self.player_ability_do_part_1)

        self.ids['game_layout_2'].add_widget(game_layout_2_button_3)
        self.ids['game_layout_2'].add_widget(game_layout_2_button_4)

    def enemy_turn(self):

        # Ход врага

        global enemies_dict, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated, \
            cells_passed, enemies_dict, the_map_passed

        for i in enemies_dict.values():

            for e in i.items():

                moving_points = e[1].moving_speed
                do_points = 1
                enemy_position = []
                player_position = []

                while moving_points != 0 and do_points != 0:

                    if e[1].damage != 0 and enemy_distance(e[0], enemy_position, player_position) <= \
                            e[1].close_fight_radius:
                        fight_cache = e[1].close_fight(player_creature)
                        self.ids['game_label_2'].text += '\n[color=ff0000]' + e[0] + \
                                                         '[/color] close attack you, your health: [color=00ff00]' + \
                                                         str(fight_cache[0]) + '[/color]([color=ff0000]-' + \
                                                         str(fight_cache[1]) + '[/color])'
                        do_points -= 1

                        damage_received += fight_cache[1]

                        if player_creature.health <= 0:
                            break

                    elif e[1].ranged_damage != 0 and enemy_distance(e[0], enemy_position, player_position) <= \
                            e[1].ranged_combat_radius:
                        fight_cache = e[1].ranged_combat(player_creature)
                        self.ids['game_label_2'].text += '\n[color=ff0000]' + e[0] + \
                                                         '[/color] ranged attack you, your health: [color=00ff00]' + \
                                                         str(fight_cache[0]) + '[/color]([color=ff0000]-' + \
                                                         str(fight_cache[1]) + '[/color])'
                        do_points -= 1

                        damage_received += fight_cache[1]

                        if player_creature.health <= 0:
                            break

                    else:
                        moving_points -= 1
                        enemy_moving(e[0])

                if player_creature.health > 0:

                    if do_points != 0 and e[1].health < e[1].max_health:
                        heal_cache = e[1].heal()
                        self.ids['game_label_2'].text += '\n[color=ff0000]' + e[0] + '[/color] health: [color=00ff00]' + \
                                                         str(heal_cache[0]) + '[/color]([color=00ff00]+' + \
                                                         str(heal_cache[1]) + '[/color])'
                        do_points -= 1
                    elif do_points != 0:
                        self.ids['game_label_2'].text += '\n[color=ff0000]' + e[0] + '[/color] doing nothing.'
                        do_points -= 1

                else:

                    break

        # Вывод характеристик игрока

        self.ids['game_label_3'].text = '[size=16]You characters:[/size]\nHealth: [color=00ff00]' + \
                                        str(player_creature.health) + '[/color]\nHealing power: [color=00ff00]' + \
                                        str(player_creature.healing_power) + \
                                        '[/color]\nClose fight damage: [color=ff0000]' + str(player_creature.damage) + \
                                        '[/color]\nRanged combat damage: [color=ff0000]' + \
                                        str(player_creature.ranged_damage) + \
                                        '[/color]\nClose fight radius: [color=ff00ff]' + \
                                        str(player_creature.close_fight_radius) + \
                                        '[/color]\nRanged combat radius: [color=ff00ff]' + \
                                        str(player_creature.ranged_combat_radius) + \
                                        '[/color]\nMoving speed: [color=00ffff]' + str(player_creature.moving_speed) + \
                                        '[/color]'

        # Вывод карты

        self.print_map()

        # Автосохранение после конца карты

        save_session(difficult, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated,
                     cells_passed, enemies_dict, self.current_save)

        # Сброс локальной статистики

        the_map_passed = {}
        for i in game_3_0_data.difficult_list:
            the_map_passed[i] = 0
        get_artifacts = 0
        enemies_killed = 0
        damage_received = 0
        damage_done = 0
        health_regenerated = 0
        cells_passed = 0

        if player_creature.health <= 0:

            self.ids['game_label_2'].text += \
                '\n[color=ff0000]You died, AHAHAHAHAHAHAHAHAHAHAHAHAHAHAH![/color]\n\nYou want watch statistic or exit?'

            # end game

            game_layout_2_button_26 = Button(text='Go to\nmenu.', on_release=self.go_menu, font_size=13)
            game_layout_2_button_27 = Button(text='Go to\nstatistic.', on_release=self.go_statistic, font_size=13)

            self.ids['game_layout_2'].add_widget(game_layout_2_button_26)
            self.ids['game_layout_2'].add_widget(game_layout_2_button_27)

            # heal player(not in label)(need because if player start new game in current window session, player
            # characters not update to default

            player_creature.health = player_creature.max_health

            # save statistics in .txt

            # read from .py

            data = open(self.current_save, 'r')

            old_data = data.readlines()

            data.close()

            new_data = ''

            for i in old_data[20:]:
                new_data += i

            # delete .py file

            remove(self.current_save)

            # create and write in .txt

            data = open(str(number_of_save) + '_save.txt', 'w')

            data.write(new_data.replace('_', ' '))

            data.close()

            # +1 to number_of_save in game_3_0_data.py

            data = open('game_3_0_data.py', 'r')

            old_data = data.readlines()

            data.close()

            old_data[12] = 'number_of_save = ' + str(int(old_data[12][17:-1]) + 1) + '\n'

            data = open('game_3_0_data.py', 'w')

            for i in old_data:
                data.write(i)

            data.close()

            saves_list.remove(self.current_save)

        else:

            self.new_turn()

    def player_moving_part_1(self, instance):

        global now_map, correct_directions, player_position

        self.ids['game_layout_2'].clear_widgets()

        if self.moving_points == '':

            n1 = 0

            for i in now_map[1:]:

                n1 += 1
                n2 = -1

                for e in i:

                    n2 += 1

                    if e == '  P':
                        player_position = [n1, n2]

            self.moving_points = player_creature.moving_speed

        if self.moving_points > 0:

            # Обнуление или создание списка корректных направлений

            correct_directions = []

            # Проверка куда можно двигаться

            global game_layout_2_button_5, game_layout_2_button_6, game_layout_2_button_7, game_layout_2_button_8, \
                game_layout_2_button_9, game_layout_2_button_10, game_layout_2_button_11, game_layout_2_button_12, \
                game_layout_2_button_13

            # 1
            try:
                if now_map[player_position[0] - 1][player_position[1] - 1] == '  `':
                    game_layout_2_button_5 = Button(text='1', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_5)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_5)
            except (TypeError, IndexError):
                pass

            # 2
            try:
                if now_map[player_position[0] - 1][player_position[1]] == '  `':
                    game_layout_2_button_6 = Button(text='2', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_6)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_6)
            except (TypeError, IndexError):
                pass

            # 3
            try:
                if now_map[player_position[0] - 1][player_position[1] + 1] == '  `':
                    game_layout_2_button_7 = Button(text='3', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_7)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_7)
            except (TypeError, IndexError):
                pass

            # 4
            try:
                if now_map[player_position[0]][player_position[1] + 1] == '  `':
                    game_layout_2_button_8 = Button(text='4', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_8)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_8)
            except (TypeError, IndexError):
                pass

            # 5
            try:
                if now_map[player_position[0] + 1][player_position[1] + 1] == '  `':
                    game_layout_2_button_9 = Button(text='5', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_9)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_9)
            except (TypeError, IndexError):
                pass

            # 6
            try:
                if now_map[player_position[0] + 1][player_position[1]] == '  `':
                    game_layout_2_button_10 = Button(text='6', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_10)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_10)
            except (TypeError, IndexError):
                pass

            # 7
            try:
                if now_map[player_position[0] + 1][player_position[1] - 1] == '  `':
                    game_layout_2_button_11 = Button(text='7', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_11)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_11)
            except (TypeError, IndexError):
                pass

            # 8
            try:
                if now_map[player_position[0]][player_position[1] - 1] == '  `':
                    game_layout_2_button_12 = Button(text='8', on_release=self.player_moving_part_2)
                    correct_directions.append(game_layout_2_button_12)
                    self.ids['game_layout_2'].add_widget(game_layout_2_button_12)
            except (TypeError, IndexError):
                pass

            game_layout_2_button_13 = Button(text='quit', on_release=self.player_moving_part_2)

            correct_directions.append(game_layout_2_button_13)

            self.ids['game_layout_2'].add_widget(game_layout_2_button_13)

            self.ids['game_label_2'].text += '\nOn why direction you want move? You moving points: ' + \
                                             str(self.moving_points)

        else:
            self.ids['game_label_2'].text += '\nYou don`t have more moving points('
            self.moving_points = ''
            return self.player_ability_do_part_1('')

    def player_moving_part_2(self, instance):

        global correct_directions, player_position, now_map

        self.ids['game_layout_2'].clear_widgets()

        direction_move = instance.text

        if direction_move == 'quit':
            self.ids['game_label_2'].text += '\nYou decided to quit from moving'
            self.moving_points = ''
            return self.player_ability_do_part_1('')

        # Изменение позиции на карте

        now_map[player_position[0]][player_position[1]] = '  `'

        if direction_move == '1':
            now_map[player_position[0] - 1][player_position[1] - 1] = '  P'
            player_position[0] -= 1
            player_position[1] -= 1
            self.ids['game_label_2'].text += '\nYou moved on 1 direction'
        if direction_move == '2':
            now_map[player_position[0] - 1][player_position[1]] = '  P'
            player_position[0] -= 1
            self.ids['game_label_2'].text += '\nYou moved on 2 direction'
        if direction_move == '3':
            now_map[player_position[0] - 1][player_position[1] + 1] = '  P'
            player_position[0] -= 1
            player_position[1] += 1
            self.ids['game_label_2'].text += '\nYou moved on 3 direction'
        if direction_move == '4':
            now_map[player_position[0]][player_position[1] + 1] = '  P'
            player_position[1] += 1
            self.ids['game_label_2'].text += '\nYou moved on 4 direction'
        if direction_move == '5':
            now_map[player_position[0] + 1][player_position[1] + 1] = '  P'
            player_position[0] += 1
            player_position[1] += 1
            self.ids['game_label_2'].text += '\nYou moved on 5 direction'
        if direction_move == '6':
            now_map[player_position[0] + 1][player_position[1]] = '  P'
            player_position[0] += 1
            self.ids['game_label_2'].text += '\nYou moved on 6 direction'
        if direction_move == '7':
            now_map[player_position[0] + 1][player_position[1] - 1] = '  P'
            player_position[0] += 1
            player_position[1] -= 1
            self.ids['game_label_2'].text += '\nYou moved on 7 direction'
        if direction_move == '8':
            now_map[player_position[0]][player_position[1] - 1] = '  P'
            player_position[1] -= 1
            self.ids['game_label_2'].text += '\nYou moved on 8 direction'

        global cells_passed

        cells_passed += 1

        self.moving_points -= 1

        self.print_map()

        self.ids['game_layout_2'].clear_widgets()

        self.player_moving_part_1('')

    def player_ability_do_part_1(self, instance):

        global ability_can_list

        if instance != '':

            if instance.text == 'No':
                self.ids['game_layout_2'].clear_widgets()

        # Использование способностей

        ability_can_list = ['doing nothing']
        ability_can_list_painted = ['Doing nothing']

        # Health check

        if player_creature.health < player_creature.max_health:
            ability_can_list.append('heal')
            ability_can_list_painted.append('Heal')

        # Close fight check

        for i in distance().items():

            if player_creature.close_fight_radius >= i[1]:
                ability_can_list.append(i[0][1:].lower() + ' close attack')
                ability_can_list_painted.append('[color=ff0000]' + i[0][1:] + '[/color] close attack')

        # Range attack check

        for i in distance().items():

            if player_creature.ranged_combat_radius >= i[1]:
                ability_can_list.append(i[0][1:].lower() + ' ranged attack')
                ability_can_list_painted.append('[color=ff0000]' + i[0][1:] + '[/color] ranged attack')

        ability_can_str = '\n'
        n = 0

        for i in ability_can_list_painted:
            n += 1

            ability_can_str += str(n) + '. ' + i + '.\n'

        self.ids['game_label_2'].text += '\nWhat you do?' + ability_can_str

        if len(ability_can_list) > 9:

            global game_layout_2_button_14, game_layout_2_label_6, game_layout_2_button_15, game_layout_2_button_16

            game_layout_2_button_14 = Button(text='+', on_release=self.label_6_plus)
            game_layout_2_label_6 = Label(text='1')
            game_layout_2_button_15 = Button(text='-', on_release=self.label_6_minus)
            game_layout_2_button_16 = Button(text='Upload', on_release=self.player_ability_do_part_2)

            self.ids['game_layout_2'].add_widget(game_layout_2_button_14)
            self.ids['game_layout_2'].add_widget(game_layout_2_label_6)
            self.ids['game_layout_2'].add_widget(game_layout_2_button_15)
            self.ids['game_layout_2'].add_widget(game_layout_2_button_16)

        else:

            game_layout_2_button_17 = Button(text='1', on_release=self.player_ability_do_part_2)
            game_layout_2_button_18 = Button(text='2', on_release=self.player_ability_do_part_2)
            game_layout_2_button_19 = Button(text='3', on_release=self.player_ability_do_part_2)
            game_layout_2_button_20 = Button(text='4', on_release=self.player_ability_do_part_2)
            game_layout_2_button_21 = Button(text='5', on_release=self.player_ability_do_part_2)
            game_layout_2_button_22 = Button(text='6', on_release=self.player_ability_do_part_2)
            game_layout_2_button_23 = Button(text='7', on_release=self.player_ability_do_part_2)
            game_layout_2_button_24 = Button(text='8', on_release=self.player_ability_do_part_2)
            game_layout_2_button_25 = Button(text='9', on_release=self.player_ability_do_part_2)

            global button_list

            button_list = [game_layout_2_button_17, game_layout_2_button_18, game_layout_2_button_19,
                           game_layout_2_button_20, game_layout_2_button_21, game_layout_2_button_22,
                           game_layout_2_button_23, game_layout_2_button_24, game_layout_2_button_25]

            for i in range(len(ability_can_list)):
                self.ids['game_layout_2'].add_widget(button_list[i])

    def player_ability_do_part_2(self, instance):

        global ability_can_list, enemies_dict, now_map, button_list, player_artefacts, get_artifacts, enemies_killed, \
            damage_received, damage_done, health_regenerated, cells_passed, enemies_dict, the_map_passed

        # clear label if too many symbols

        if len(self.ids['game_label_2'].text) >= 1400:

            n = 0

            for i in self.ids['game_label_2'].text[:1000]:

                if i == '\n':

                    self.ids['game_label_2'].text = self.ids['game_label_2'].text[1000 + n:]

                    break

                n += 1

        if instance.text == 'Upload':

            ability_choose = game_layout_2_label_6.text

            if int(ability_choose) not in [i for i in range(len(ability_can_list))]:

                self.ids['game_label_2'].text += '\nWrong number!!! Try again.'

                return

        else:

            ability_choose = instance.text

        # Выполнение выбранной способности

        # Ничего не делать

        if ability_choose == '1':

            self.ids['game_label_2'].text += '\nYou didn`t do anything'

        # Лечение

        elif ability_choose == '2' and ability_can_list[1] == 'heal':

            heal_cache = player_creature.heal()

            self.ids['game_label_2'].text += '\n[color=00ff00]You[/color] health: [color=00ff00]' + \
                                             str(heal_cache[0]) + '[/color]([color=00ff00]+' + str(heal_cache[1]) + \
                                             '[/color])'

            health_regenerated += heal_cache[1]

        # Ближняя и дальняя атаки

        elif 'close attack' in ability_can_list[int(ability_choose) - 1] or 'ranged attack' in \
                ability_can_list[int(ability_choose) - 1]:

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

            self.ids['game_label_2'].text += '\n[color=ff0000]' + enemy_name + '[/color] health: [color=00ff00]' + \
                                             str(fight_cache[0]) + '[/color]([color=ff0000]-' + str(fight_cache[1]) + \
                                             '[/color])'

            damage_done += fight_cache[1]

            n = 0
            del_list = []

            for i in enemies_dict.values():

                n += 1

                for e in i.items():

                    if e[0] == enemy_name:

                        if e[1].health <= 0:

                            self.ids['game_label_2'].text += '\n\nYou killed [color=ff0000]' + e[0] + \
                                                             '[/color], my congratulations.\n'

                            del_list.append(n)

                            n1 = 0

                            for u in now_map[1:]:

                                n1 += 1
                                n2 = -1

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

            for i in del_list:
                del enemies_dict['Enemy_' + str(i)]

            # after delete dictionary can look like {'Enemy_1': enemy_1, 'Enemy_3': enemy_3}, it will cause
            # iteration error in further code. For prevent this we do 'Enemy_3; -> 'Enemy_2' in dictionary.

            if del_list:

                enemies_killed += 1

                self.print_map()

                n = 0
                new_enemies_dict = {}

                for i in enemies_dict.items():

                    n += 1

                    if i[0][6:] != str(n):

                        new_enemies_dict['Enemy_' + str(n)] = enemies_dict[i[0]]

                    else:

                        new_enemies_dict[i[0]] = i[1]

                enemies_dict = copy.deepcopy(new_enemies_dict)

        enemy_names = []

        # Выводим характеристик(и) врагов(а)

        self.print_enemies_characters()

        if not enemies_dict:

            self.ids['game_label_5'].text = 'All clear.'

            self.ids['game_label_2'].text += '\n\nYou kill all enemies! You complete this map!\n'

            # give random artefact

            if type(player_artefacts) == dict:

                p = player_artefacts

            else:

                p = player_artefacts.player_artefacts_list

            global difficult

            received_artefact = random_artefact(difficult)

            p[received_artefact] += 1

            self.ids['game_label_2'].text += '\nYou received ' + \
                                             received_artefact.replace('_', ' ')[:len(received_artefact) - 1] + \
                                             '[font=font4.ttf]' + received_artefact[len(received_artefact) - 1:] + \
                                             '[/font]'

            self.print_artefacts()

            # save game

            get_artifacts += 1

            the_map_passed[difficult] += 1

            difficult = 'in_hub'

            save_session('in_hub', get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated,
                         cells_passed, enemies_dict, self.current_save)

            # Сброс локальной статистики

            the_map_passed = {}
            for i in game_3_0_data.difficult_list:
                the_map_passed[i] = 0
            get_artifacts = 0
            enemies_killed = 0
            damage_received = 0
            damage_done = 0
            health_regenerated = 0
            cells_passed = 0

            # start new map

            self.ids['game_layout_2'].clear_widgets()

            self.ids['game_label_2'].text += '\n\nClick to push your [color=ff00ff]luck[/color].'

            game_layout_2_button_28 = Button(text='[color=ff00ff]Luck test.[/color]', markup=True,
                                             on_release=self.build_game)

            self.ids['game_layout_2'].add_widget(game_layout_2_button_28)

            # heal player(not in label)

            player_creature.health = player_creature.max_health

            return

        # Удаление уже лишних виджетов

        self.ids['game_layout_2'].clear_widgets()

        self.enemy_turn()

    def build_game(self, instance):

        from game_3_0_enemies import enemies_dict_names, enemies_dict_const

        # create new save file if not exist

        if not path.exists(self.current_save):
            check_save(self.current_save)

        # import current save as "saves" for more comfort code work

        global saves, difficult

        if self.current_save in ['', 'Yes']:

            self.current_save = instance

        elif self.current_save == 'save_1.py':
            import save_1 as saves

        elif self.current_save == 'save_2.py':
            import save_2 as saves

        elif self.current_save == 'save_3.py':
            import save_3 as saves

        self.ids['game_layout_2'].clear_widgets()

        global player_creature, player_artefacts, player_creature, now_map, difficult, enemies_dict, all_map_const, \
            difficult, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated, \
            cells_passed, enemies_dict, the_map_passed

        importlib.reload(game_3_0_data)

        the_map_passed = {}
        for i in game_3_0_data.difficult_list:
            the_map_passed[i] = 0
        get_artifacts = 0
        enemies_killed = 0
        damage_received = 0
        damage_done = 0
        health_regenerated = 0
        cells_passed = 0

        # Проверка saves

        if check_save(self.current_save):

            # импорт данных из saves

            importlib.reload(saves)

            difficult = saves.status

            player_artefacts = saves.player_artefacts

            if difficult != 'in_hub':

                now_map = saves.now_map
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
                        enemies_dict['Enemy_' + str(number_of_enemy)][e] = copy.deepcopy(enemies_dict_names[e])
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

                now_map = copy.deepcopy(all_maps_const[difficult])

                # Определяем позиции(ю) врагов(а) на карте

                crop_number = round(len(now_map) / 2)

                enemies_number = game_3_0_data.max_map_enemies[difficult]

                enemies_dict = {}
                enemies_numbers = {}
                enemy_names = []
                enemies_list = []
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

                                # numbers_of_enemies += 1

                                enemies_list.append(choice)

                                # if choice in enemies_numbers.keys():

                                #    enemies_numbers[choice] += 1

                                #    #enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                                #    #    choice + ' ' + str(enemies_numbers[choice]): copy.deepcopy(enemies_dict_names[
                                #    #                                                                   choice + ' ' + str(
                                #    #                                                                       enemies_numbers[
                                #    #                                                                           choice])])}

                                # else:

                                #    enemies_numbers[choice] = 1

                                #    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                                #        choice + ' ' + str(enemies_numbers[choice]): copy.deepcopy(enemies_dict_names[
                                #                                                                       choice + ' ' + str(
                                #                                                                           enemies_numbers[
                                #                                                                               choice])])}

                                c = all_choices.count(choice) + 1

                                all_choices.append(choice)

                                choice = ' ' + choice[0] + str(c)

                                enemies_number -= 1

                                now_map[i][e] = choice

                enemies_list.sort()

                for i in enemies_list:

                    numbers_of_enemies += 1

                    if i in enemies_numbers.keys():

                        enemies_numbers[i] += 1

                        enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                            i + ' ' + str(enemies_numbers[i]): copy.deepcopy(enemies_dict_names[
                                                                                 i + ' ' + str(
                                                                                     enemies_numbers[
                                                                                         i])])}
                    else:

                        enemies_numbers[i] = 1

                        enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                            i + ' ' + str(enemies_numbers[i]): copy.deepcopy(enemies_dict_names[
                                                                                 i + ' ' + str(
                                                                                     enemies_numbers[
                                                                                         i])])}
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

            now_map = copy.deepcopy(all_maps_const[difficult])

            # Определяем позиции(ю) врагов(а) на карте

            crop_number = round(len(now_map) / 2)

            enemies_number = game_3_0_data.max_map_enemies[difficult]

            enemies_dict = {}
            enemies_numbers = {}
            enemy_names = []
            enemies_list = []
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

                            #numbers_of_enemies += 1

                            enemies_list.append(choice)

                            #if choice in enemies_numbers.keys():

                            #    enemies_numbers[choice] += 1

                            #    #enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                            #    #    choice + ' ' + str(enemies_numbers[choice]): copy.deepcopy(enemies_dict_names[
                            #    #                                                                   choice + ' ' + str(
                            #    #                                                                       enemies_numbers[
                            #    #                                                                           choice])])}

                            #else:

                            #    enemies_numbers[choice] = 1

                            #    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                            #        choice + ' ' + str(enemies_numbers[choice]): copy.deepcopy(enemies_dict_names[
                            #                                                                       choice + ' ' + str(
                            #                                                                           enemies_numbers[
                            #                                                                               choice])])}

                            c = all_choices.count(choice) + 1

                            all_choices.append(choice)

                            choice = ' ' + choice[0] + str(c)

                            enemies_number -= 1

                            now_map[i][e] = choice

            enemies_list.sort()

            for i in enemies_list:

                numbers_of_enemies += 1

                if i in enemies_numbers.keys():

                    enemies_numbers[i] += 1

                    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                        i + ' ' + str(enemies_numbers[i]): copy.deepcopy(enemies_dict_names[
                                                                                     i + ' ' + str(
                                                                                        enemies_numbers[
                                                                                              i])])}
                else:

                    enemies_numbers[i] = 1

                    enemies_dict['Enemy_' + str(numbers_of_enemies)] = {
                        i + ' ' + str(enemies_numbers[i]): copy.deepcopy(enemies_dict_names[
                                                                                   i + ' ' + str(
                                                                                       enemies_numbers[
                                                                                           i])])}

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

        enemy_names = []

        self.ids['game_label_2'].text += '\nYour map difficult now: ' + difficult

        # Выводим текущую карту

        self.print_map()

        # Выводим характеристик(и) врагов(а)

        self.print_enemies_characters()

        # Вывод характеристик игрока

        self.print_player_characters()

        # Выводим артефакты

        self.print_artefacts()

        # Движение

        self.ids['game_label_2'].text += '\nYou need move?'

        game_layout_2_button_3 = Button(text='Yes', on_release=self.player_moving_part_1)
        game_layout_2_button_4 = Button(text='No', on_release=self.player_ability_do_part_1)

        self.ids['game_layout_2'].add_widget(game_layout_2_button_3)
        self.ids['game_layout_2'].add_widget(game_layout_2_button_4)


class CustomizerScreen(Screen):
    pass


class AddMapScreen(Screen):

    def build(self):

        str_artefacts_list = '[size=11][u]'

        n = 1
        k = 0

        for i in game_3_0_data.artefact_do.keys():

            if n == len(game_3_0_data.artefact_do.keys()):

                str_artefacts_list += i + '[/u].[/size]'

            else:

                n += 1

                if k > 30:

                    k = 0

                    str_artefacts_list += '\n' + i + '[/u], [u]'

                    k += len('\n' + i + ', ')

                else:

                    str_artefacts_list += i + '[/u], [u]'

                    k += len(i + ', ')

        str_enemies_list = '[u]'

        n = 1
        k = 0

        for i in game_3_0_data.enemies_indexes.keys():

            if n == len(game_3_0_data.enemies_indexes.keys()):

                str_enemies_list += i + '[/u].'

            else:

                n += 1

                if k > 30:

                    k = 0

                    str_enemies_list += '\n' + i + '[/u], [u]'

                    k += len('\n' + i + ', ')

                else:

                    str_enemies_list += i + '[/u], [u]'

                    k += len(i + ', ')

        self.ids['add_map_extra_label_1'].text += str_artefacts_list
        self.ids['add_map_extra_label_2'].text += str_enemies_list

    def check(self):

        incorrect_list = []

        if self.ids['add_map_text_input_1'].text.isnumeric() or \
                '\\' in self.ids['add_map_text_input_1'].text or '&' in self.ids['add_map_text_input_1'].text or \
                self.ids['add_map_text_input_1'].text == '' or \
                self.ids['add_map_text_input_1'].text in game_3_0_data.difficult_list:

            incorrect_list.append('1')

        if not self.ids['add_map_text_input_2'].text.isnumeric() or self.ids['add_map_text_input_2'].text == '':

            incorrect_list.append('2')

        if not self.ids['add_map_text_input_3'].text.isnumeric() or self.ids['add_map_text_input_3'].text == '':

            incorrect_list.append('3')

        if not self.ids['add_map_text_input_4'].text.isnumeric() or self.ids['add_map_text_input_4'].text == '':

            incorrect_list.append('4')

        if self.ids['add_map_text_input_5'].text.isnumeric() or \
                '\\' in self.ids['add_map_text_input_5'].text or '&' in self.ids['add_map_text_input_5'].text or \
                self.ids['add_map_text_input_5'].text == '':

            incorrect_list.append('5')

        else:

            map_artefacts_list = []

            n = ''

            text = self.ids['add_map_text_input_5'].text.replace(' ', '').lower()

            for i in text:

                if i == ',':

                    map_artefacts_list.append(n)

                    n = ''

                else:

                    n += i

            if not map_artefacts_list:
                map_artefacts_list.append(text)

            for i in map_artefacts_list:

                if i not in game_3_0_data.artefact_do.keys():

                    incorrect_list.append('5')

                    break

        if not self.ids['add_map_text_input_6'].text.isnumeric() or \
                '\\' in self.ids['add_map_text_input_6'].text or '&' in self.ids['add_map_text_input_6'].text or \
                self.ids['add_map_text_input_6'].text == '':

            incorrect_list.append('6')

        else:

            map_artefacts_chances = []

            n = ''

            text = self.ids['add_map_text_input_6'].text.replace(' ', '')

            for i in text:

                if i != ',' and not i.isnumeric():

                    incorrect_list.append('6')

                    break

                if i == ',':

                    map_artefacts_chances.append(int(n))

                    n = ''

                else:

                    n += i

        if self.ids['add_map_text_input_7'].text.isnumeric() or \
                '\\' in self.ids['add_map_text_input_7'].text or '&' in self.ids['add_map_text_input_7'].text or \
                self.ids['add_map_text_input_7'].text == '':

            incorrect_list.append('7')

        else:

            map_enemies_list = []

            n = ''

            text = self.ids['add_map_text_input_7'].text.replace(' ', '')

            for i in text:

                if i == ',':

                    map_enemies_list.append(n)

                    n = ''

                else:

                    n += i

            if not map_enemies_list:
                map_enemies_list.append(text)

            for i in map_enemies_list:

                if i not in game_3_0_data.enemies_indexes.keys():

                    incorrect_list.append('7')

                    break

        if not self.ids['add_map_text_input_8'].text.isnumeric() or self.ids['add_map_text_input_8'].text == '':

            incorrect_list.append('8')

        # if all correct made map, else print incorrect value in: 1, 2... labels.

        if incorrect_list:

            self.ids['add_map_label_0'].text = 'Incorrect value in: '

            n = 0

            for i in incorrect_list:

                n += 1

                if n == len(incorrect_list):

                    self.ids['add_map_label_0'].text += i + '.\nCheck it and try again.\n[size=13](Check commas, ' \
                                                            'artefact/enemies exist and correct spelling of words, ' \
                                                            'try another names.)[/size]'

                else:

                    self.ids['add_map_label_0'].text += i + ', '

        else:

            self.ids['add_map_label_0'].text = 'Map made successful.'

            import game_3_0_customizer

            return game_3_0_customizer.made_map(self.ids['add_map_text_input_1'].text.lower(),
                                                int(self.ids['add_map_text_input_2'].text),
                                                int(self.ids['add_map_text_input_3'].text),
                                                int(self.ids['add_map_text_input_4'].text),
                                                map_artefacts_list,
                                                map_artefacts_chances,
                                                map_enemies_list,
                                                int(self.ids['add_map_text_input_8'].text))


class AddEnemyScreen(Screen):

    def build(self):

        str_map_list = '[u]'

        n = 1
        k = 0

        for i in game_3_0_data.difficult_list:

            if n == len(game_3_0_data.difficult_list):

                str_map_list += i + '[/u].'

            else:

                n += 1

                if k > 30:

                    k = 0

                    str_map_list += '\n' + i + '[/u], [u]'

                    k += len('\n' + i + ', ')

                else:

                    str_map_list += i + '[/u], [u]'

                    k += len(i + ', ')

        self.ids['add_enemy_extra_label_1'].text += str_map_list

    def check(self):

        incorrect_list = []

        if not self.ids['add_enemy_text_input_1'].text.isnumeric() or self.ids['add_enemy_text_input_1'].text == '':
            incorrect_list.append('1')

        if not self.ids['add_enemy_text_input_2'].text.isnumeric() or self.ids['add_enemy_text_input_2'].text == '':
            incorrect_list.append('2')

        if not self.ids['add_enemy_text_input_3'].text.isnumeric() or self.ids['add_enemy_text_input_3'].text == '':
            incorrect_list.append('3')

        if not self.ids['add_enemy_text_input_5'].text.isnumeric() or self.ids['add_enemy_text_input_5'].text == '':
            incorrect_list.append('5')

        if not self.ids['add_enemy_text_input_6'].text.isnumeric() or self.ids['add_enemy_text_input_6'].text == '':
            incorrect_list.append('6')
        if not self.ids['add_enemy_text_input_7'].text.isnumeric() or self.ids['add_enemy_text_input_7'].text == '':
            incorrect_list.append('7')

        if not self.ids['add_enemy_text_input_8'].text.isnumeric() or self.ids['add_enemy_text_input_8'].text == '':
            incorrect_list.append('8')

        if self.ids['add_enemy_text_input_9'].text.isnumeric() or '\\' in self.ids['add_enemy_text_input_9'].text or \
                '&' in self.ids['add_enemy_text_input_9'].text or self.ids['add_enemy_text_input_9'].text == '':

            incorrect_list.append('9')

        else:

            enemy_maps_list = []

            n = ''

            text = self.ids['add_enemy_text_input_9'].text.replace(' ', '')

            for i in text:

                if i == ',':

                    enemy_maps_list.append(n)

                    n = ''

                else:

                    n += i

            if not enemy_maps_list:
                enemy_maps_list.append(text)

            for i in enemy_maps_list:

                if i not in game_3_0_data.difficult_list:
                    incorrect_list.append('9')

                    break

        if self.ids['add_enemy_text_input_10'].text.isnumeric() or '\\' in self.ids['add_enemy_text_input_10'].text or \
                '&' in self.ids['add_enemy_text_input_10'].text or self.ids['add_enemy_text_input_10'].text == '' or \
                not self.ids['add_enemy_text_input_10'].text[0].isupper() or \
                self.ids['add_enemy_text_input_10'].text in game_3_0_data.enemies_indexes.keys():

            incorrect_list.append('10')

        # if all correct made enemy, else print incorrect value in: 1, 2... labels.

        if incorrect_list:

            self.ids['add_enemy_label_0'].text = 'Incorrect value in: '

            n = 0

            for i in incorrect_list:

                n += 1

                if n == len(incorrect_list):

                    self.ids['add_enemy_label_0'].text += i + '.\nCheck it and try again.\n[size=13](Check commas, ' \
                                                              'map exist and correct spelling of words, ' \
                                                              'try another names[/size])'

                else:

                    self.ids['add_enemy_label_0'].text += i + ', '

        else:

            self.ids['add_enemy_label_0'].text = 'enemy made successful.'

            import game_3_0_customizer

            return game_3_0_customizer.made_enemy(int(self.ids['add_enemy_text_input_1'].text),
                                                  int(self.ids['add_enemy_text_input_2'].text),
                                                  int(self.ids['add_enemy_text_input_3'].text),
                                                  int(self.ids['add_enemy_text_input_4'].text),
                                                  int(self.ids['add_enemy_text_input_5'].text),
                                                  int(self.ids['add_enemy_text_input_6'].text),
                                                  int(self.ids['add_enemy_text_input_7'].text),
                                                  int(self.ids['add_enemy_text_input_8'].text),
                                                  enemy_maps_list,
                                                  self.ids['add_enemy_text_input_10'].text)


class AddArtefactScreen(Screen):

    def build(self):

        artefact_map = '[u]'

        n = 1
        k = 0

        for i in game_3_0_data.difficult_list:

            if n == len(game_3_0_data.difficult_list):

                artefact_map += i + '[/u].'

            else:

                n += 1

                if k > 30:

                    k = 0

                    artefact_map += '\n' + i + '[/u], [u]'

                    k += len('\n' + i + ', ')

                else:

                    artefact_map += i + '[/u], [u]'

                    k += len(i + ', ')

        self.ids['add_artefact_extra_label_1'].text += artefact_map

    def check(self):

        incorrect_list = []

        if self.ids['add_artefact_text_input_1'].text.isnumeric() or \
                self.ids['add_artefact_text_input_1'].text == '' or \
                '\\' in self.ids['add_artefact_text_input_1'].text or \
                '&' in self.ids['add_artefact_text_input_1'].text or \
                self.ids['add_artefact_text_input_1'].text in game_3_0_data.artefact_do.keys():
            incorrect_list.append('1')

        if self.ids['add_artefact_text_input_2'].text.isnumeric() or \
                self.ids['add_artefact_text_input_2'].text == '' or \
                '\\' in self.ids['add_artefact_text_input_2'].text or \
                '&' in self.ids['add_artefact_text_input_2'].text or \
                '+' not in self.ids['add_artefact_text_input_2'].text and \
                '-' not in self.ids['add_artefact_text_input_2'].text:
            incorrect_list.append('2')

        if not self.ids['add_artefact_text_input_3'].text.isnumeric() or \
                self.ids['add_artefact_text_input_3'].text == '':
            incorrect_list.append('3')

        if not self.ids['add_artefact_text_input_4'].text.isnumeric() or \
                self.ids['add_artefact_text_input_4'].text == '':
            incorrect_list.append('4')

        if not self.ids['add_artefact_text_input_5'].text.isnumeric() or \
                self.ids['add_artefact_text_input_5'].text == '':
            incorrect_list.append('5')

        if self.ids['add_artefact_text_input_6'].text.isnumeric() or \
                '\\' in self.ids['add_artefact_text_input_6'].text or \
                '&' in self.ids['add_artefact_text_input_6'].text or self.ids['add_artefact_text_input_6'].text == '':

            incorrect_list.append('6')

        else:

            artefact_maps_list = []

            n = ''

            text = self.ids['add_artefact_text_input_6'].text.replace(' ', '')

            for i in text:

                if i == ',':

                    artefact_maps_list.append(n)

                    n = ''

                else:

                    n += i

            if not artefact_maps_list:
                artefact_maps_list.append(text)

            for i in artefact_maps_list:

                if i not in game_3_0_data.difficult_list:
                    incorrect_list.append('6')

                    break

        if self.ids['add_artefact_text_input_7'].text.isnumeric() or \
                '\\' in self.ids['add_artefact_text_input_7'].text or \
                '&' in self.ids['add_artefact_text_input_7'].text or self.ids['add_artefact_text_input_7'].text == '':

            incorrect_list.append('7')

        else:

            artefact_what_do_list = []

            n = ''

            text = self.ids['add_artefact_text_input_7'].text.replace(' ', '')

            for i in text:

                if i == ',':

                    artefact_what_do_list.append(n)

                    n = ''

                else:

                    n += i

            if not artefact_what_do_list:
                artefact_what_do_list.append(text)

            for i in artefact_what_do_list:

                if i not in ['health', 'damage', 'ranged_damage', 'close_fight_radius', 'ranged_combat_radius',
                             'moving_speed', 'healing_power', 'max_health']:
                    incorrect_list.append('7')

                    break

        # if all correct made artefact, else print incorrect value in: 1, 2... labels.

        if incorrect_list:

            self.ids['add_artefact_label_0'].text = 'Incorrect value in: '

            n = 0

            for i in incorrect_list:

                n += 1

                if n == len(incorrect_list):

                    self.ids['add_artefact_label_0'].text += i + '.\nCheck it and try again.\n[size=13](Check commas,' \
                                                                 ' map exist and correct spelling of words, ' \
                                                                 'try another names.)[/size]'

                else:

                    self.ids['add_artefact_label_0'].text += i + ', '

        else:

            self.ids['add_artefact_label_0'].text = 'artefact made successful.'

            import game_3_0_customizer

            return game_3_0_customizer.made_artefact(self.ids['add_artefact_text_input_1'].text.lower(),
                                                     self.ids['add_artefact_text_input_2'].text,
                                                     int(self.ids['add_artefact_text_input_3'].text),
                                                     int(self.ids['add_artefact_text_input_4'].text),
                                                     int(self.ids['add_artefact_text_input_5'].text),
                                                     artefact_maps_list,
                                                     artefact_what_do_list)


class SettingsScreen(Screen):
    pass


class StatisticScreen(Screen):

    def build(self):
        global number_of_save

        data = open(str(number_of_save) + '_save.txt', 'r')

        old_data = data.readlines()

        data.close()

        number_of_save += 1

        data = ''

        for i in old_data:
            data += i

        global game_label_7

        self.ids['statistic_label_1'].text = 'You died:(((((\n\n' + data.replace('_', ' ').replace(' =', ':')


class GameApp(App):

    def build(self):

        Builder.load_string(kv)

        Window.size = (830, 625)

        # Set minimum window size

        Window.minimum_width = Window.size[0]
        Window.minimum_height = Window.size[1]

        # Make ScreenManager

        global sm

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(CustomizerScreen(name='customizer'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(StatisticScreen(name='statistic'))
        sm.add_widget(SaveChooseScreen(name='save_choose'))
        sm.add_widget(AddMapScreen(name='add_map'))
        sm.add_widget(AddEnemyScreen(name='add_enemy'))
        sm.add_widget(AddArtefactScreen(name='add_artefact'))

        return sm


def random_artefact(map_name):
    # Открываем и забираем данные из файла

    data = open('game_3_0_data.py', 'r')

    old_data = data.readlines()

    data.close()

    # Берём нужную строку с данными карты по артефактам

    old_data_map_string = old_data[game_3_0_data.map_indexes[map_name]]

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

    return received_artefact


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

    enemy_position_save = copy.deepcopy(enemy_position)

    # 1 направление

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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

    enemy_position = copy.deepcopy(enemy_position_save)

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


def check_save(save_name):
    if not path.exists(save_name):
        data = open(save_name, 'w+')

        data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                   'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                   '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

        n = 20

        for i in game_3_0_data.difficult_list:
            data.write(i + '_passed = 0' + '\n')

            n += 1

        data.write(
            'get_artifacts = 0\nenemies_killed = 0\ndamage_received = 0\ndamage_done = 0\nhealth_regenerated = 0\n'
            'cells_passed = 0\n')

        data.close()

        return False

    else:
        data = open(save_name, 'r')

        old_data = data.readlines()

        data.close()

        data = open(save_name, 'r')

        old_data_str = data.read()

        data.close()

        stat_check = ['get_artifacts = \n', 'enemies_killed = \n', 'damage_received = \n', 'damage_done = \n',
                      'health_regenerated = \n', 'cells_passed = \n']
        stat_check_str = ''

        n = 0

        for i in game_3_0_data.difficult_list:
            stat_check.insert(n, i + '_passed = \n')

            stat_check_str += i + '_passed = 0\n'

            n += 1

        old_data_stat = []

        # replace all numbers on '' for check statistic

        for i in range(len(old_data[20:26 + len(game_3_0_data.difficult_list)])):

            old_data_stat_cache = old_data[20:26 + len(game_3_0_data.difficult_list)][i]

            for e in [str(i) for i in range(0, 10)]:

                old_data_stat_cache = old_data_stat_cache.replace(e, '')

            old_data_stat.append(old_data_stat_cache)

        if old_data_str == '0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё Р' \
                           'ёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n# РЎС‚Р°С‚РёСЃС' \
                           '‚РёРєР°:\n\n' + stat_check_str + 'get_artifacts = 0\nenemies_killed = 0\ndamage_received ' \
                                                             '= 0\ndamage_done = 0\nhealth_regenerated = 0\n' \
                                                             'cells_passed = 0\n':

            return False

        elif len(old_data) != 26 + len(game_3_0_data.difficult_list) or old_data_stat != stat_check:

            data = open(save_name, 'w+')

            data.write('0\n\n# РљР°СЂС‚Р°:\n\n0\n\n# РђСЂС‚РµС„Р°РєС‚С‹:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё '
                       'РёРіСЂРѕРєР°:\n\n0\n\n# РҐР°СЂР°РєС‚РµСЂРёСЃС‚РёРєРё РІСЂР°РіРѕРІ:\n\n0\n\n'
                       '# РЎС‚Р°С‚РёСЃС‚РёРєР°:\n\n')

            n = 20

            for i in game_3_0_data.difficult_list:
                data.write(i + '_passed = 0' + '\n')

                n += 1

            data.write(
                'get_artifacts = 0\nenemies_killed = 0\ndamage_received = 0\ndamage_done = 0\nhealth_regenerated = 0\n'
                'cells_passed = 0\n')

            data.close()

            return False

        else:

            return True


def save_session(status, get_artifacts, enemies_killed, damage_received, damage_done, health_regenerated, cells_passed,
                 enemies_dict, current_save):

    global player_artefacts, now_map, the_map_passed

    # статус это название карты или in_hub

    # сохраняем всё важное(данные игрока, статус игры, данные врагов и статистику

    # Проверка существования файла и его правильности по количеству строк

    importlib.reload(saves)

    check_save(current_save)

    # Открываем и читаем файл

    data = open(current_save, 'r')

    old_data = data.readlines()

    data.close()

    # Заносим текущий статус

    old_data[0] = 'status = "' + status + '"\n'

    # Заносим карту

    if status != 'in_hub':

        old_data[4] = 'now_map = ' + str(now_map) + '\n'

    else:

        old_data[4] = 'now_map = {}\n'

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

    if enemies_dict:

        for i in enemies_dict.items():
            for e in i[1].items():

                if numbers_of_enemies == 0:
                    numbers_of_enemies += 1
                    part_1 = 'enemies_dict = {"Enemy_' + str(numbers_of_enemies) + '": {'
                    old_data[16] = part_1 + '"{}": [{}, {}, {}, {}, {}, {}, {}, {}]'.format(e[0], e[1].health,
                                                                                            e[1].damage,
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

    else:

        old_data[16] = 'enemies_dict = {}\n'

    # Заносим статистику

    n = 20

    for i in game_3_0_data.difficult_list:
        k = old_data[n][len(i) + 10:-1]

        old_data[n] = i + '_passed = ' + str(int(k) + the_map_passed[i]) + '\n'

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

    new_data = open(current_save, 'w')

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

        if len(enemies_positions_list) == game_3_0_data.max_map_enemies[difficult] and player_position != []:
            break

        if i == len(now_map):
            break

        i += 1

        if i == len(now_map):
            break

        for e in range(len(now_map[i])):

            if now_map[i][e] != '  `' and now_map[i][e] != '  P' and now_map[i][e] != '#':
                enemies_positions_list.append([i, e])
                enemies_distance[now_map[i][e]] = 0

            if now_map[i][e] == '  P':
                player_position = [i, e]

            if len(enemies_positions_list) == game_3_0_data.max_map_enemies[difficult] and player_position != []:
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
