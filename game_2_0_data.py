difficult_list = ["easy", "medium"]
difficult_weights = [60, 4000]
all_maps = {"easy": [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']], "medium": [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']]}

map_indexes = {'easy': 12, 'medium': 13}
enemies_indexes = {'Baron': 53, 'Elsa': 56}

start_player_artefacts = {'sharpening_stone_1': 1, 'sharpening_stone_2': 0, 'hard_skin_potion_1': 0, 'hard_skin_potion_2': 0, 'turkey_plumage_1': 0, 'turkey_plumage_2': 0}
artefact_do = {'sharpening_stone_1': ['+', ['ranged_damage', 'damage'], 5], 'sharpening_stone_2': ['+', ['ranged_damage', 'damage'], 10], 'hard_skin_potion_1': ['+', ['health'], 20], 'hard_skin_potion_2': ['+', ['health'], 40], 'turkey_plumage_1': ['+', ['ranged_combat_radius'], 1], 'turkey_plumage_2': ['+', ['ranged_combat_radius'], 2]}

max_map_enemies = {'easy': 1, 'medium': 2}

easy_map_artefact_chances = {'sharpening_stone_1': 35, 'hard_skin_potion_1': 40, 'turkey_plumage_1': 25}
medium_map_artefact_chances = {'sharpening_stone_1': 20, 'sharpening_stone_2': 10, 'hard_skin_potion_1': 35, 'hard_skin_potion_2': 20, 'turkey_plumage_1': 10, 'turkey_plumage_2': 5}
