# Prints information for a single run in a human readable format


def details(current_run):
    indent = '  '
    double_indent = indent + indent
    print('General stats:')
    print("%s Character chosen: %s" % (indent, current_run.character_chosen))
    print("%s Ascension: %s" % (indent, current_run.ascension))
    print("%s Victory: %s" % (indent, current_run.victory))
    print("%s Floor reached: %s" % (indent, current_run.floor_reached))
    print("%s Campfire rested: %s" % (indent, current_run.campfire_rested))
    print("%s Campfire upgrades: %s" % (indent, current_run.campfire_upgraded))
    print("%s Total Gold Gained: %s" % (indent, current_run.total_gold_gained))
    print("%s Total Gold Spent/Lost: %s" % (indent, current_run.total_gold_lost))
    print('\n')

    print("Act 1:")
    print("%s Boss relic picked act one: %s" % (indent, current_run.boss_relic_picked_act1))
    print("%s Boss relic not picked act one: %s" % (indent, current_run.boss_relic_not_picked_act1))

    print("Act 2:")
    print("%s Boss relic picked act two: %s" % (indent, current_run.boss_relic_picked_act2))
    print("%s Boss relic not picked act two: %s" % (indent, current_run.boss_relic_not_picked_act2))


def file_name(current_run):
    print("  File Name: %s" % current_run.id)


def ascension(current_run):
    print("    Ascension: %s" % current_run.ascension)


def boss_relic_picked_act1(current_run):
    print("    Boss Relic picked Act One: %s" % current_run.boss_relic_picked_act1)


def boss_relic_not_picked_act1(current_run):
    print("    Boss relic not picked Act One: %s" % current_run.boss_relic_not_picked_act1)


def boss_relic_picked_act2(current_run):
    print("    Boss Relic picked Act Two: %s" % current_run.boss_relic_picked_act2)


def boss_relic_not_picked_act2(current_run):
    print("    Boss relic not picked Act Two: %s" % current_run.boss_relic_not_picked_act2)


def build_version(current_run):
    print("    Build Version: %s" % current_run.build_version)


def campfire_rested(current_run):
    print("    Campfire Rested: %s" % current_run.campfire_rested)


def campfire_upgraded(current_run):
    print("    Campfire Upgraded: %s" % current_run.campfire_upgraded)


def character_chosen(current_run):
    print("    Character Chosen: %s" % current_run.character_chosen)


def chosen_seed(current_run):
    print("    Chosen Seed: %s" % current_run.chosen_seed)


def circlet_count(current_run):
    print("    Circlet Count: %s" % current_run.circlet_count)


def floor_reached(current_run):
    print("    Floor Reached: %s" % current_run.floor_reached)


def gold(current_run):
    print("    Gold: %s" % current_run.gold)


def is_ascension_mode(current_run):
    print("    Is Ascension Mode: %s" % current_run.is_ascension_mode)


def is_daily(current_run):
    print("    Is Daily: %s" % current_run.is_daily)


def is_endless(current_run):
    print("    Is Endless: %s" % current_run.is_endless)


def is_prod(current_run):
    print("    Is Prod: %s" % current_run.is_prod)


def is_trial(current_run):
    print("    Is Trial: %s" % current_run.is_trial)


def neow_bonus(current_run):
    print("    Neow Bonus: %s" % current_run.neow_bonus)


def neow_cost(current_run):
    print("    Neow Cost: %s" % current_run.neow_cost)


def play_id(current_run):
    print("    Play Id: %s" % current_run.play_id)


def player_experience(current_run):
    print("    Player Experience: %s" % current_run.player_experience)


def playtime(current_run):
    print("    Playtime: %s" % current_run.playtime)


def purchased_purges(current_run):
    print("    Purchased Purges: %s" % current_run.purchased_purges)


def score(current_run):
    print("    Score: %s" % current_run.score)


def seed_played(current_run):
    print("    Seed Played: %s" % current_run.seed_played)


def seed_source_timestamp(current_run):
    print("    Seed Source Timestamp: %s" % current_run.seed_source_timestamp)


def special_seed(current_run):
    print("    Special Seed: %s" % current_run.special_seed)


def timestamp(current_run):
    print("    Timestamp: %s" % current_run.timestamp)


def victory(current_run):
    print("    Victory: %s" % current_run.victory)


def win_rate(current_run):
    print("    Win Rate: %s" % current_run.win_rate)


def campfire_choices(current_run):
    if current_run.campfire_choices:
        print("  Campfire Choices:")

        for x in current_run.campfire_choices:
            if x.data:
                print("    Floor: %s || Action: %s || Data: %s" % (x.floor, x.key, x.data))
            else:
                print("    Floor: %s || Action: %s" % (x.floor, x.key))


def card_choices(current_run):
    print("  Card Choices:")
    for card in current_run.card_choices:
        print('    Floor: %s || Picked: %s || Not Picked: %s' % (card.floor, card.picked, card.not_picked))


def current_hp_per_floor(current_run):
    print("  Current HP per floor")
    floor_count = 0
    for current_hp in current_run.current_hp_per_floor:
        print("    Floor: %s || Current HP: %s" % (floor_count, current_hp))
        floor_count += 1


def event_choices(current_run):
    print("  Event Choices:")
    for x in current_run.event_choices:
        print("    Floor: %s" % x.floor)
        print("      Event Name: %s" % x.event_name)
        print("      Player Choice: %s" % x.player_choice)
        print("      Damage Taken: %s" % x.damage_taken)


def damage_taken(current_run):
    print("  Damage Taken:")
    for x in current_run.damage_taken:
        print("    Floor: %s" % x.floor)
        print("      Enemies: %s" % x.enemies)
        print("      Turns: %s" % x.turns)
        print("      Damage: %s" % x.damage)


def gold_per_floor(parsed, current_run):
    # TODO: Remove for loop and read from 'Run' class file
    indent = '  '
    new_line = '\n'
    double_indent = indent + indent
    floor_number = 1
    previous_gold_value = 0
    total_gold_gained = 0
    total_gold_lost = 0

    print("%sGold Per Floor:" % indent)

    for element in parsed['gold_per_floor']:
        current_floor = double_indent + "Floor: %s" % floor_number
        current_gold = double_indent + "Gold: %s" % element
        final_string = current_floor + new_line + indent + current_gold

        if floor_number == 1:
            final_string += new_line + double_indent + indent + 'Diff: +' + str(element - current_run.starting_gold)
            total_gold_gained += element - current_run.starting_gold
            current_run.add_gold_diff_per_floor(element - current_run.starting_gold)
        elif floor_number != 1:
            if element - previous_gold_value == 0:
                final_string += ' (No Change)'
            elif element - previous_gold_value != 0:
                if element - previous_gold_value > 0:
                    final_string += new_line + double_indent + indent + 'Diff: +' + str(element - previous_gold_value)
                    total_gold_gained += element - previous_gold_value
                else:
                    final_string += new_line + double_indent + indent + 'Diff: ' + str(element - previous_gold_value)
                    total_gold_lost += element - previous_gold_value
            current_run.add_gold_diff_per_floor(element - previous_gold_value)
        else:
            print('Unexpected result... with printing gold_per_floor_all')

        previous_gold_value = element

        current_run.add_gold_for_floor(element)
        current_run.add_total_gold_gained(total_gold_gained)
        current_run.add_total_gold_lost(total_gold_lost)

        print(final_string)
        print("%s %s Total Gained: +%s" % (double_indent, indent, total_gold_gained))
        print("%s %s Total Spent/Lost %s" % (double_indent, indent, total_gold_lost))
        floor_number += 1

    return current_run


def items_purchased(current_run):
    print('  Items Purchased:')
    for item_purchased in current_run.items_purchased:
        print('    ', item_purchased)


def master_deck(current_run):
    print("  Master Deck:")
    for card in current_run.master_deck:
        print("    ", card)


def max_hp_per_floor(current_run):
    print("  Max HP Per Floor:")
    floor_count = 0
    for max_hp in current_run.max_hp_per_floor:
        print("    Floor: %s || Max HP: %s" % (floor_count, max_hp))
        floor_count += 1


def path_per_floor(current_run):
    print("  Path Per Floor:")
    for path in current_run.path_per_floor:
        print("    ", path)


def path_taken_per_floor(current_run):
    print("  Path Taken:")
    for path_taken in current_run.path_taken:
        print("    ", path_taken)


def potions_floor_spawned(current_run):
    print('  Potions Spawned Per Floor:')
    for potion in current_run.potions_floor_spawned:
        print("    ", potion)


def potions_floor_usage(current_run):
    print('  Potions Used Per Floor:')
    for potion in current_run.potions_floor_usage:
        print("    ", potion)


def potions_obtained(current_run):
    print('  Potion Obtained Per Floor:')
    for detail in current_run.potions_obtained:
        print("    Floor: %s || Potion: %s" % (detail.floor, detail.key))


def relics(current_run):
    print('  Relics:')
    for relic in current_run.relics:
        print('    ', relic)


def relics_obtained(current_run):
    print('  Relics Obtained:')
    for relic_obtained in current_run.relics_obtained:
        print("    Floor: %s || Relic: %s" % (relic_obtained.floor, relic_obtained.key))
