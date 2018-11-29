

def two_indent_list():
    return ['OverviewIndividual',
            'CampfireStats'
            'CampfireChoices',
            'TotalCampfiresVisited',
            'AvgCampfiresVisited',
            'TotalCampfiresRested',
            'AvgCampfiresRested',
            'TotalCampfiresUpgraded',
            'AvgCampfiresUpgraded',
            'CampfireRestPerFloor',
            'CurrentHpPerFloor',
            'CardChoices',
            'DamageTaken',
            'EventChoices',
            'ItemsPurchased',
            'MasterDeck',
            'GoldPerFloor',
            'ItemsPurchased',
            'MasterDeck',
            'MaxHpPerFloor',
            'PathPerFloor',
            'PathTakenPerFloor',
            'PotionsFloorSpawned',
            'PotionsFloorUsage',
            'PotionsObtained',
            'Relics',
            'RelicsObtained']


def four_indent_list():
    return ['BuildVersion',
            'Timestamp',
            'SpecialSeed',
            'SeedPlayed',
            'CharacterChosen',
            'Ascension',
            'Victory',
            'WinRate',
            'FloorReached',
            'Score',
            'NeowBonus',
            'NeowCost',
            'CampfireRested',
            'CampfireUpgraded',
            'ChosenSeed',
            'CircletCount',
            'Gold',
            'IsAscensionMode',
            'IsDaily',
            'IsEndless',
            'IsProd',
            'IsTrial',
            'PlayId',
            'PlayerExperience',
            'Playtime',
            'PurchasedPurges',
            'SeedSourceTimestamp',
            'BossRelicPickedActOne',
            'BossRelicNotPickedActOne',
            'BossRelicPickedActTwo',
            'BossRelicNotPickedActTwo']


def create_title_header(title):
    bookend = ''
    bookend_length = len(title) + 6
    complete_header = ''

    complete_header += '\n'
    for x in range(0, bookend_length):
        bookend += '*'

    complete_header += "%s\n** %s ** \n%s\n\n" % (bookend, title, bookend)

    return complete_header


def avg_campfires_visited(average):
    if average > 0:
        print('Average number of campfires visited per playthrough: %s' % average)
    else:
        print("There was an issue calculating the avg_campfires_visited")


def individual_run(printable_config_items):
    two_idents_items = two_indent_list()
    four_indents_items = four_indent_list()

    for config_item in printable_config_items:
        if config_item.section == 'PRINT_INDIVIDUAL_RUN':
            if config_item.config_item_name in two_idents_items:
                print("  %s" % config_item.console_message)
            elif config_item.config_item_name in four_indents_items:
                print("    %s" % config_item.console_message)
            else:
                print("No indenting has been provided for %s" % config_item.config_item_name)
                print(config_item.console_message)

    print()


def all_runs(printable_config_items):
    for config_item in printable_config_items:
        if config_item.section == 'PRINT_ALL_RUNS':
            print(config_item.console_message)
    print()
