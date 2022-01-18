difficult_list = ["easy", "medium"]
difficult_weights = [60, 40]
all_maps = {"easy": [0, ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], "medium": [0, ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], ['#', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `', ' `'], 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]}

map_indexes = {'easy': 10, 'medium': 11}
enemies_indexes = {'enemy_creature_1': 134, 'enemy_creature_2': 135}

start_player_artefacts = {'sharpening_stone_1': 1, 'sharpening_stone_2': 0, 'hard_skin_potion_1': 0, 'hard_skin_potion_2': 0, 'turkey_plumage_1': 0, 'turkey_plumage_2': 0}
artefact_do = {'sharpening_stone_1': ['+', ['ranged_damage', 'damage'], 5], 'sharpening_stone_2': ['+', ['ranged_damage', 'damage'], 10], 'hard_skin_potion_1': ['+', ['health'], 20], 'hard_skin_potion_2': ['+', ['health'], 40], 'turkey_plumage_1': ['+', ['ranged_combat_radius'], 1], 'turkey_plumage_2': ['+', ['ranged_combat_radius'], 2]}

easy_map_artefact_chances = {'sharpening_stone_1': 35, 'hard_skin_potion_1': 40, 'turkey_plumage_1': 25}
medium_map_artefact_chances = {'sharpening_stone_1': 20, 'sharpening_stone_2': 10, 'hard_skin_potion_1': 35, 'hard_skin_potion_2': 20, 'turkey_plumage_1': 10, 'turkey_plumage_2': 5}
