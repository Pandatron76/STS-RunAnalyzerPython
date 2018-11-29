# Stores the json list information from the .run_data file into an STSRun object

from run_data.card_choices import CardChoices
from run_data.damage_taken import DamageTaken
from run_data.event_choices import EventChoices
from run_data.potions_obtained import PotionsObtained
from run_data.relics_obtained import RelicsObtained


# Users can only pick one boss relic
def boss_relic_info(current_run, parsed):
    act_count = 0
    for relic in parsed['boss_relics']:
        if isinstance(None, type(relic.get('picked'))) is False:
            if relic['picked']:
                if act_count == 0:
                    current_run.add_boss_relic_picked_act1(relic['picked'])
                elif act_count == 1:
                    current_run.add_boss_relic_picked_act2(relic['picked'])
                else:
                    print('Issue with boss relic/picked')
        elif isinstance(None, type(relic.get('picked'))) is True:
            if act_count == 0:
                current_run.add_boss_relic_picked_act1('No boss relic was picked for Act One')
            elif act_count == 1:
                current_run.add_boss_relic_picked_act2('No boss relic was picked for Act Two')
            else:
                print('Issue with boss relic/picked')
        else:
            print('Issue determining if [boss_relic][picked] is a None type')

        if isinstance(None, type(relic.get('not_picked'))) is False:
            if relic['not_picked']:
                for relic_np in relic['not_picked']:
                    if act_count == 0:
                        current_run.add_boss_relic_not_picked_act1(relic_np)
                    elif act_count == 1:
                        current_run.add_boss_relic_not_picked_act2(relic_np)
                    else:
                        print('Issue with boss relic/not picked')
        elif isinstance(None, type(relic.get('not_picked'))) is True:
            if act_count == 0:
                current_run.add_boss_relic_picked_act1('No boss relic was not picked for Act One')
            elif act_count == 1:
                current_run.add_boss_relic_picked_act2('No boss relic was not picked for Act Two')
            else:
                print('Issue with boss relic/picked')
        else:
            print('Issue determining if [boss_relic][not_picked] is a None type')

        act_count += act_count + 1
    return current_run


def card_choices(current_run, parsed):
    if 'card_choices' in parsed:
        for element in parsed['card_choices']:
            current_card_choices = CardChoices()

            current_card_choices.add_floor(element.get('floor'))
            current_card_choices.add_picked(element.get('picked'))
            current_card_choices.add_not_picked(element.get('not_picked'))
            current_run.add_card_choices(current_card_choices)

    return current_run


def current_hp_per_floor(current_run, parsed):
    # Store the values form the run_data file
    if 'current_hp_per_floor' in parsed:
        for element in parsed['current_hp_per_floor']:
            current_run.add_current_hp_for_floor(element)


def damage_taken(current_run, parsed):
    # Store the values form the run_data file
    if 'damage_taken' in parsed:
        for element in parsed['damage_taken']:
            run_damage_taken = DamageTaken()

            run_damage_taken.add_damage(element.get('damage'))
            run_damage_taken.add_enemies(element.get('enemies'))
            run_damage_taken.add_floor(element.get('floor'))
            run_damage_taken.add_turns(element.get('turns'))

            current_run.add_damage_taken(run_damage_taken)


def event_choices(current_run, parsed):
    # Store the value from the run_data file
    if 'event_choices' in parsed:
        for element in parsed['event_choices']:
            run_event_choices = EventChoices()

            run_event_choices.add_damage_taken(element.get('damage_taken'))
            run_event_choices.add_event_name(element.get('event_name'))
            run_event_choices.add_floor(element.get('floor'))
            run_event_choices.add_player_choice(element.get('player_choice'))

            current_run.add_event_choices(run_event_choices)


def gold_per_floor_all(current_run, parsed):
    for gold in parsed['gold_per_floor']:
        current_run.add_gold_for_floor(gold)


def items_purchased_all(current_run, parsed):
    if 'items_purchased' in parsed:
        for item in parsed['items_purchased']:
            current_run.add_items_purchased(item)


def master_deck_all(current_run, parsed):
    if 'master_deck' in parsed:
        for card in parsed['master_deck']:
            current_run.add_master_deck(card)


def max_hp_per_floor_all(current_run, parsed):
    if 'max_hp_per_floor' in parsed:
        for max_hp in parsed['max_hp_per_floor']:
            current_run.add_max_hp_per_floor(max_hp)


def path_per_floor(current_run, parsed):
    for path in parsed['path_per_floor']:
        current_run.add_path_per_floor(path)
    return current_run


def path_taken(current_run, parsed):
    for taken in parsed['path_taken']:
        current_run.add_path_taken(taken)
    return current_run


def potions_floor_spawned(current_run, parsed):
    for potion in parsed['potions_floor_spawned']:
        current_run.add_potions_floor_spawned(potion)
    return current_run


def potions_floor_usage(current_run, parsed):
    for potion in parsed['potions_floor_usage']:
        current_run.add_potions_floor_usage(potion)
    return current_run


def potions_obtained(current_run, parsed):
    if 'potions_obtained' in parsed:
        for element in parsed['potions_obtained']:
            run_potions_obtained = PotionsObtained()

            run_potions_obtained.add_floor(element.get('floor'))
            run_potions_obtained.add_key(element.get('key'))
            current_run.add_potions_obtained(run_potions_obtained)

    return current_run


def relics(current_run, parsed):
    for relic in parsed['relics']:
        current_run.add_relics(relic)
    return current_run


# TODO: Refactor to store the value in the sts_run_data as a dict rather than a 'relics_obtained' object
def relics_obtained(current_run, parsed):
    if 'relics_obtained' in parsed:
        for element in parsed['relics_obtained']:
            run_relics_obtained = RelicsObtained()

            run_relics_obtained.add_floor(element.get('floor'))
            run_relics_obtained.add_key(element.get('key'))
            current_run.add_relics_obtained(run_relics_obtained)

    return current_run
