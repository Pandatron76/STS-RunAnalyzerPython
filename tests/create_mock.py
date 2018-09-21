from sts_run_history_analyzer.sts_run_data import *
import configparser


def config():
    mock_config = configparser.ConfigParser()
    mock_config.optionxform = str

    mock_config['DIRECTORIES'] = {'TargetPath': '',
                                  'CharactersToInclude': 'DEFECT,THE_SILENT,IRONCLAD'}

    mock_config['PRINT_ALL_RUNS'] = {'Overview': 'False',
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

    mock_config['PRINT_SINGLE_RUN'] = {'FileName': 'False',
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
                                       'RelicsObtained': 'False',
                                       }

    return mock_config


def sts_run_data(run_name):
    return STSRunData(run_name)
