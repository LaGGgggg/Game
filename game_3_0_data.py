difficult_list = ["easy", "medium", "hard"]
difficult_weights = [600000, 40, 300000000000000]
all_maps = {"easy": [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']], "medium": [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']], "hard": [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']]}

map_indexes = {'easy': 14, 'medium': 15, "hard": 16}
enemies_indexes = {'Baron': 76, 'Elsa': 87, "Lucius": 98}

start_player_artefacts = {'sharpening_stone_1': 2, 'sharpening_stone_2': 2, 'hard_skin_potion_1': 1, 'hard_skin_potion_2': 1, 'turkey_plumage_1': 1, 'turkey_plumage_2': 1}
artefact_do = {'sharpening_stone_1': ['+', ['ranged_damage', 'damage'], 5], 'sharpening_stone_2': ['+', ['ranged_damage', 'damage'], 10], 'hard_skin_potion_1': ['+', ['health'], 20], 'hard_skin_potion_2': ['+', ['health'], 40], 'turkey_plumage_1': ['+', ['ranged_combat_radius'], 1], 'turkey_plumage_2': ['+', ['ranged_combat_radius'], 2]}

max_map_enemies = {'easy': 1, 'medium': 2, 'hard': 10}

number_of_save = 25

easy_map_artefact_chances = {'sharpening_stone_1': 35, 'hard_skin_potion_1': 40, 'turkey_plumage_1': 25}
medium_map_artefact_chances = {'sharpening_stone_1': 20, 'sharpening_stone_2': 10, 'hard_skin_potion_1': 35, 'hard_skin_potion_2': 20, 'turkey_plumage_1': 10, 'turkey_plumage_2': 5}
hard_map_artefact_chances = {"hard_skin_potion_1": 5, "turkey_plumage_2": 3, "sharpening_stone_1": 20}
