status = "hard"

# Карта:

now_map = [0, ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', ' E1', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', ' B2', ' B5', ' E4', ' B4', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  P', ' E3', ' E2', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', ' B3', ' B1', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', ' L1', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `'], ['#', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `', '  `']]

# Артефакты:

player_artefacts = {'sharpening_stone_1': 1, 'sharpening_stone_2': 0, 'hard_skin_potion_1': 0, 'hard_skin_potion_2': 0, 'turkey_plumage_1': 0, 'turkey_plumage_2': 0}

# Характеристики игрока:

player_creature = [18, 15, 10, 1, 3, 3, 15, 100]

# Характеристики врагов:

enemies_dict = {"Enemy_1": {"Elsa 1": [200, 1, 2, 1, 1, 1, 1, 200]}, "Enemy_2": {"Baron 1": [11, 1, 1, 1, 1, 1, 1, 10]}, "Enemy_3": {"Baron 2": [11, 1, 1, 1, 1, 1, 1, 10]}, "Enemy_4": {"Lucius 1": [100, 10, 0, 2, 0, 2, 20, 100]}, "Enemy_5": {"Elsa 2": [200, 1, 2, 1, 1, 1, 1, 200]}, "Enemy_6": {"Baron 3": [11, 1, 1, 1, 1, 1, 1, 10]}, "Enemy_7": {"Baron 4": [11, 1, 1, 1, 1, 1, 1, 10]}, "Enemy_8": {"Elsa 3": [200, 1, 2, 1, 1, 1, 1, 200]}, "Enemy_9": {"Baron 5": [11, 1, 1, 1, 1, 1, 1, 10]}, "Enemy_10": {"Elsa 4": [200, 1, 2, 1, 1, 1, 1, 200]}}

# Статистика:

easy_passed = 0
medium_passed = 0
hard_passed = 0
get_artifacts = 0
enemies_killed = 0
damage_received = 0
damage_done = 0
health_regenerated = 0
cells_passed = 0
