import configparser

from run_data.sts_run_data import *
from config.config_item import *


def all_false_config():
    mock_config = configparser.ConfigParser()
    mock_config.optionxform = str

    mock_config['DIRECTORIES'] = {'TargetPath': '',
                                  'CharactersToInclude': 'DEFECT,THE_SILENT,IRONCLAD'}

    mock_config['PRINT_INDIVIDUAL_RUN'] = {'Overview': 'False',
                                     'AvgCampfiresVisited': 'False',
                                     'AvgCampfiresRested': 'False',
                                     'AvgCampfiresUpgraded': 'False',
                                     'AvgFloorReached': 'False',
                                     'AvgScore': 'False',
                                     'CampfireRestPerFloor': 'False',
                                     'CampfireStats': 'False',
                                     'CampfireUpgradedPerFloor': 'False',
                                     'CardsPickedPerFloor': 'False',
                                     'CumulativeDamagePerEnemy': 'False',
                                     'EnemyEncounterCount': 'False',
                                     'EnemiesEncounteredPerFloor': 'False',
                                     'EventChoicesPerFloor': 'False',
                                     'HighestMaxHP': 'False',
                                     'HighestScore': 'False',
                                     'ItemsPurchasedCount': 'False',
                                     'LowestMaxHP': 'False',
                                     'LowestScore': 'False',
                                     'PotionsDataSpawned': 'False',
                                     'PotionsDataUsed': 'False',
                                     'PotionsDataObtained': 'False',
                                     'MostGold': 'False',
                                     'RelicCount': 'False',
                                     'TotalCampfiresVisited': 'False',
                                     'TotalCampfiresRested': 'False',
                                     'TotalCampfiresUpgraded': 'False',
                                     'WinLostRecords': 'False'}

    mock_config['PRINT_INDIVIDUAL_RUN'] = {'FileName': 'False',
                                       'Overview': 'False',
                                       'Ascension': 'False',
                                       'BuildVersion': 'False',
                                       'CampfireRested': 'False',
                                       'CampfireUpgraded': 'False',
                                       'CharacterChosen': 'False',
                                       'ChosenSeed': 'False',
                                       'CircletCount': 'False',
                                       'FloorReached': 'False',
                                       'Gold': 'False',
                                       'IsAscensionMode': 'False',
                                       'IsDaily': 'False',
                                       'IsEndless': 'False',
                                       'IsProd': 'False',
                                       'IsTrial': 'False',
                                       'NeowBonus': 'False',
                                       'NeowCost': 'False',
                                       'PlayId': 'False',
                                       'PlayerExperience': 'False',
                                       'Playtime': 'False',
                                       'PurchasedPurges': 'False',
                                       'Score': 'False',
                                       'SeedPlayed': 'False',
                                       'SeedSourceTimestamp': 'False',
                                       'SpecialSeed': 'False',
                                       'Timestamp': 'False',
                                       'Victory': 'False',
                                       'WinRate': 'False',
                                       'BossRelicPickedActOne': 'False',
                                       'BossRelicNotPickedActOne': 'False',
                                       'BossRelicPickedActTwo': 'False',
                                       'BossRelicNotPickedActTwo': 'False',
                                       'CampfireChoices': 'False',
                                       'CardChoices': 'False',
                                       'CurrentHpPerFloor': 'False',
                                       'DamageTaken': 'False',
                                       'EventChoices': 'False',
                                       'GoldPerFloor': 'False',
                                       'ItemsPurchased': 'False',
                                       'MasterDeck': 'False',
                                       'MaxHpPerFloor': 'False',
                                       'PathPerFloor': 'False',
                                       'PathTakenPerFloor': 'False',
                                       'PotionsFloorSpawned': 'False',
                                       'PotionsFloorUsage': 'False',
                                       'PotionsObtained': 'False',
                                       'Relics': 'False',
                                       'RelicsObtained': 'False'}

    return mock_config


def all_true_config():
    mock_config = configparser.ConfigParser()
    mock_config.optionxform = str

    mock_config['DIRECTORIES'] = {'TargetPath': '',
                                  'CharactersToInclude': 'DEFECT,THE_SILENT,IRONCLAD'}

    mock_config['PRINT_INDIVIDUAL_RUNS'] = {'Overview': 'True',
                                     'AvgCampfiresVisited': 'True',
                                     'AvgCampfiresRested': 'True',
                                     'AvgCampfiresUpgraded': 'True',
                                     'AvgFloorReached': 'True',
                                     'AvgScore': 'True',
                                     'CampfireRestPerFloor': 'True',
                                     'CampfireStats': 'True',
                                     'CampfireUpgradedPerFloor': 'True',
                                     'CardsPickedPerFloor': 'True',
                                     'CumulativeDamagePerEnemy': 'True',
                                     'EnemyEncounterCount': 'True',
                                     'EnemiesEncounteredPerFloor': 'True',
                                     'EventChoicesPerFloor': 'True',
                                     'HighestMaxHP': 'True',
                                     'HighestScore': 'True',
                                     'ItemsPurchasedCount': 'True',
                                     'LowestMaxHP': 'True',
                                     'LowestScore': 'True',
                                     'PotionsDataSpawned': 'True',
                                     'PotionsDataUsed': 'True',
                                     'PotionsDataObtained': 'True',
                                     'MostGold': 'True',
                                     'RelicCount': 'True',
                                     'TotalCampfiresVisited': 'True',
                                     'TotalCampfiresRested': 'True',
                                     'TotalCampfiresUpgraded': 'True',
                                     'WinLostRecords': 'True'}

    mock_config['PRINT_INDIVIDUAL_RUN'] = {'FileName': 'True',
                                       'Overview': 'True',
                                       'Ascension': 'True',
                                       'BuildVersion': 'True',
                                       'CampfireRested': 'True',
                                       'CampfireUpgraded': 'True',
                                       'CharacterChosen': 'True',
                                       'ChosenSeed': 'True',
                                       'CircletCount': 'True',
                                       'FloorReached': 'True',
                                       'Gold': 'True',
                                       'IsAscensionMode': 'True',
                                       'IsDaily': 'True',
                                       'IsEndless': 'True',
                                       'IsProd': 'True',
                                       'IsTrial': 'True',
                                       'NeowBonus': 'True',
                                       'NeowCost': 'True',
                                       'PlayId': 'True',
                                       'PlayerExperience': 'True',
                                       'Playtime': 'True',
                                       'PurchasedPurges': 'True',
                                       'Score': 'True',
                                       'SeedPlayed': 'True',
                                       'SeedSourceTimestamp': 'True',
                                       'SpecialSeed': 'True',
                                       'Timestamp': 'True',
                                       'Victory': 'True',
                                       'WinRate': 'True',
                                       'BossRelicPickedActOne': 'True',
                                       'BossRelicNotPickedActOne': 'True',
                                       'BossRelicPickedActTwo': 'True',
                                       'BossRelicNotPickedActTwo': 'True',
                                       'CampfireChoices': 'True',
                                       'CardChoices': 'True',
                                       'CurrentHpPerFloor': 'True',
                                       'DamageTaken': 'True',
                                       'EventChoices': 'True',
                                       'GoldPerFloor': 'True',
                                       'ItemsPurchased': 'True',
                                       'MasterDeck': 'True',
                                       'MaxHpPerFloor': 'True',
                                       'PathPerFloor': 'True',
                                       'PathTakenPerFloor': 'True',
                                       'PotionsFloorSpawned': 'True',
                                       'PotionsFloorUsage': 'True',
                                       'PotionsObtained': 'True',
                                       'Relics': 'True',
                                       'RelicsObtained': 'True'}

    return mock_config


def sts_run_data(run_name):
    return STSRunData(run_name)


def config_item(config_item_name):
    return ConfigItem(config_item_name)


def config_priority_dict():
    list = config_list()
    return list


def sample_raw_json():
    return '{' \
           '"gold_per_floor":[' \
           '112,123,135,135,152,152,177,177,245,245,263,298,298,298,298,' \
           '394,394,394,394,394,394,394,394,394,394,394,181,181,181,181,' \
           '39,39,39,39,39,39,39,39,3,3,3,3,3,3,3,3,3,3,3,3],' \
           '"floor_reached":50,' \
           '"playtime":4160,' \
           '"items_purged":[],' \
           '"score":815,' \
           '"play_id":"81fbf3d3-2ba3-4361-a535-b56e296c7269",' \
           '"local_time":"20180915224954",' \
           '"is_ascension_mode":true,' \
           '"campfire_choices":[{"data":"Uppercut","floor":6,"key":"SMITH"},' \
           '{"floor":10,"key":"DIG"},{"floor":15,"key":"DIG"},' \
           '{"floor":23,"key":"REST"},{"floor":28,"key":"DIG"},' \
           '{"floor":32,"key":"REST"},{"floor":40,"key":"REST"},' \
           '{"floor":42,"key":"REST"},{"data":"Limit Break","floor":45,"key":"SMITH"},' \
           '{"floor":47,"key":"REST"},{"data":"Power Through","floor":49,"key":"SMITH"}],' \
           '"neow_cost":"NONE",' \
           '"seed_source_timestamp":10728044479451,' \
           '"circlet_count":0,' \
           '"master_deck":["Strike_R","Strike_R","Strike_R","Strike_R","Defend_R",' \
           '"Defend_R","Defend_R","Defend_R","Bash","AscendersBane",' \
           '"Uppercut+1","Headbutt","Shrug It Off+1","Sword Boomerang","Fiend Fire",' \
           '"Power Through+1","Feed","Pommel Strike","Inflame+1","True Grit",' \
           '"Limit Break+1","Feel No Pain","Cleave","Impervious","Metallicize",' \
           '"Exhume","Feel No Pain","Evolve","Heavy Blade+1"],' \
           '"relics":["Burning Blood","Shovel","Self Forming Clay","Centennial Puzzle","Bronze Scales",' \
           '"Question Card","Boot","Ectoplasm","Omamori","Blue Candle",' \
           '"Eternal Feather","Letter Opener","Bag of Marbles"],' \
           '"potions_floor_usage":[5,7,12,16,22,30,33,46,50],' \
           '"damage_taken":[{"damage":7,"enemies":"Small Slimes","floor":1,"turns":4},' \
           '{"damage":0,"enemies":"Cultist","floor":2,"turns":3},' \
           '{"damage":2,"enemies":"Jaw Worm","floor":3,"turns":3},' \
           '{"damage":13,"enemies":"Lots of Slimes","floor":5,"turns":5},' \
           '{"damage":9,"enemies":"Lagavulin","floor":7,"turns":6},' \
           '{"damage":3,"enemies":"Looter","floor":11,"turns":3},' \
           '{"damage":12,"enemies":"Gremlin Nob","floor":12,"turns":3},' \
           '{"damage":66,"enemies":"Hexaghost","floor":16,"turns":11},' \
           '{"damage":10,"enemies":"Shell Parasite","floor":18,"turns":5},' \
           '{"damage":1,"enemies":"Chosen","floor":19,"turns":4},' \
           '{"damage":22,"enemies":"Centurion and Healer","floor":21,"turns":6},' \
           '{"damage":1,"enemies":"Colosseum Slavers","floor":22,"turns":3},' \
           '{"damage":33,"enemies":"Snecko","floor":24,"turns":5},' \
           '{"damage":30,"enemies":"Shelled Parasite and Fungi","floor":29,"turns":5},' \
           '{"damage":4,"enemies":"Snake Plant","floor":30,"turns":3},' \
           '{"damage":60,"enemies":"Champ","floor":33,"turns":16},' \
           '{"damage":26,"enemies":"Orb Walker","floor":35,"turns":5},' \
           '{"damage":31,"enemies":"3 Darklings","floor":36,"turns":5},' \
           '{"damage":67,"enemies":"Nemesis","floor":41,"turns":9},' \
           '{"damage":40,"enemies":"Maw","floor":46,"turns":10},' \
           '{"damage":106,"enemies":"Awakened One","floor":50,"turns":8}],' \
           '"seed_played":"-1337038444175666015",' \
           '"potions_obtained":[{"floor":1,"key":"Block Potion"},{"floor":3,"key":"BloodPotion"},' \
           '{"floor":5,"key":"Strength Potion"},{"floor":11,"key":"FearPotion"},' \
           '{"floor":18,"key":"SkillPotion"},{"floor":29,"key":"BloodPotion"},' \
           '{"floor":36,"key":"SneckoOil"},{"floor":41,"key":"GamblersBrew"}],' \
           '"is_trial":false,' \
           '"path_per_floor":["M","M","M","?","M","R","E","?","T","R","M","E","T","?","R","B",' \
           'null,"M","M","?","M","?","R","M","?","T","$","R","M","M","$","R","B",' \
           'null,"M","M","?","$","$","R","E","R","T","$","R","M","R","$","R"],' \
           '"character_chosen":"IRONCLAD",' \
           '"items_purchased":["Limit Break","Feel No Pain","EssenceOfSteel","Metallicize","Feel No Pain"],' \
           '"campfire_rested":5,' \
           '"item_purchase_floors":[27,27,31,31,39],' \
           '"current_hp_per_floor":[79,85,88,88,81,81,78,78,78,78,81,75,75,75,75,' \
           '23,72,68,73,56,43,48,76,49,49,49,49,49,28,42,42,72,18,81,61,36,36,36,' \
           '36,81,20,65,65,65,80,46,91,91,102,0],' \
           '"gold":3,' \
           '"neow_bonus":"TEN_PERCENT_HP_BONUS",' \
           '"is_prod":false,' \
           '"is_daily":false,' \
           '"chose_seed":false,' \
           '"campfire_upgraded":3,' \
           '"win_rate":0,' \
           '"timestamp":1537066194,' \
           '"path_taken":["M","M","M","?","?","R","E","?","T","R","?","E","?","?","R","BOSS",' \
           '"M","M","?","M","?","R","?","?","T","?","R","?","M","$","R","BOSS",' \
           '"M","M","?","?","$","R","E","R","T","$","R","M","R","?","R","BOSS"],' \
           '"build_version":"2018-09-06",' \
           '"purchased_purges":0,' \
           '"victory":false,' \
           '"max_hp_per_floor":[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,' \
           '88,88,88,88,93,96,96,96,96,96,96,96,96,99,102,' \
           '102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102],' \
           '"card_choices":[{"not_picked":["Seeing Red","Blood for Blood"],"picked":"Uppercut","floor":1},' \
           '{"not_picked":["Perfected Strike","Carnage"],"picked":"Headbutt","floor":2},' \
           '{"not_picked":["Seeing Red","Warcry"],"picked":"Shrug It Off","floor":3},' \
           '{"not_picked":["Thunderclap","Heavy Blade"],"picked":"Sword Boomerang","floor":5},' \
           '{"not_picked":["Rupture","Hemokinesis","Perfected Strike"],"picked":"SKIP","floor":7},' \
           '{"not_picked":["Dark Embrace","Whirlwind"],"picked":"Power Through","floor":11},' \
           '{"not_picked":["Wild Strike","Entrench","Pummel"],"picked":"SKIP","floor":12},' \
           '{"not_picked":["Dark Embrace","Barricade","Brutality"],"picked":"Feed","floor":16},' \
           '{"not_picked":["Whirlwind","Seeing Red","Sword Boomerang"],"picked":"Pommel Strike","floor":18},' \
           '{"not_picked":["Iron Wave","Heavy Blade","Blood for Blood","Ghostly Armor"],"picked":"SKIP","floor":19},' \
           '{"not_picked":["Searing Blow","Cleave","Clash"],"picked":"Inflame+1","floor":21},' \
           '{"not_picked":["Reckless Charge","Thunderclap","Headbutt"],"picked":"True Grit","floor":24},' \
           '{"not_picked":["Armaments","Wild Strike","Flex"],"picked":"Cleave","floor":29},' \
           '{"not_picked":["Iron Wave","Bloodletting","Pummel"],"picked":"Impervious","floor":30},' \
           '{"not_picked":["Berserk","Bludgeon","Dark Embrace"],"picked":"Exhume","floor":33},' \
           '{"not_picked":["Sever Soul+1","Dropkick","Sentinel","Perfected Strike"],"picked":"SKIP","floor":35},' \
           '{"not_picked":["Perfected Strike","Cleave","Pummel+1","Clothesline"],"picked":"SKIP","floor":36},' \
           '{"not_picked":["Armaments","Shrug It Off","Iron Wave"],"picked":"Evolve","floor":41},' \
           '{"not_picked":["Anger","Uppercut+1","Searing Blow"],"picked":"Heavy Blade+1","floor":46}],' \
           '"player_experience":466519,' \
           '"relics_obtained":[{"floor":7,"key":"Shovel"},{"floor":9,"key":"Self Forming Clay"},' \
           '{"floor":10,"key":"Centennial Puzzle"},{"floor":12,"key":"Bronze Scales"},' \
           '{"floor":13,"key":"Question Card"},{"floor":15,"key":"Boot"},' \
           '{"floor":26,"key":"Omamori"},{"floor":28,"key":"Blue Candle"},' \
           '{"floor":41,"key":"Letter Opener"},{"floor":43,"key":"Bag of Marbles"}],' \
           '"event_choices":[{"event_name":"Bonfire Elementals","player_choice":"BASIC","floor":4,"damage_taken":0},' \
           '{"event_name":"Match and Keep!","player_choice":"1 cards matched","floor":8,"damage_taken":0},' \
           '{"event_name":"Living Wall","player_choice":"Grow","floor":14,"damage_taken":0},' \
           '{"event_name":"Forgotten Altar","player_choice":"Shed Blood","floor":20,"damage_taken":0},' \
           '{"event_name":"Colosseum","player_choice":"Fight","floor":22,"damage_taken":0},' \
           '{"event_name":"Colosseum","player_choice":"Fled From Nobs","floor":22,"damage_taken":0},' \
           '{"event_name":"The Woman in Blue","player_choice":"Bought 0 Potions","floor":25,"damage_taken":0},' \
           '{"event_name":"Mysterious Sphere","player_choice":"Ignore","floor":37,"damage_taken":0}],' \
           '"is_beta":false,' \
           '"boss_relics":[{"not_picked":["Sozu","Philosopher\u0027s Stone"],"picked":"Ectoplasm"},' \
           '{"not_picked":["Runic Dome","Snecko Eye"],"picked":"Eternal Feather"}],' \
           '"items_purged_floors":[],' \
           '"is_endless":false,' \
           '"potions_floor_spawned":[1,3,5,11,18,22,29,36,41],' \
           '"killed_by":"Awakened One","ascension_level":12}'
