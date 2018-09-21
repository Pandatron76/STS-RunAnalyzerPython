# Stores information from the json into an STSRun object

from campfire import Campfire
from card_choices import CardChoices
from event_choices import EventChoices
from damage_taken import DamageTaken
from potions_obtained import PotionsObtained
from relics_obtained import RelicsObtained


# Users can only pick one boss relic
def boss_relic_info(parsed, current_run):
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


def card_choices(parsed, current_run):
    if 'card_choices' in parsed:
        for element in parsed['card_choices']:
            current_card_choices = CardChoices()

            current_card_choices.add_floor(element.get('floor'))
            current_card_choices.add_picked(element.get('picked'))
            current_card_choices.add_not_picked(element.get('not_picked'))
            current_run.add_card_choices(current_card_choices)

    return current_run


def campfire_choice(parsed, current_run):
    if 'campfire_choices' in parsed:
        for element in parsed['campfire_choices']:
            current_campfire_choice = Campfire()

            current_campfire_choice.add_floor(element.get('floor'))
            current_campfire_choice.add_key(element.get('key'))
            current_campfire_choice.add_data(element.get('data'))
            current_run.add_campfire_choices(current_campfire_choice)

    return current_run


def current_hp_per_floor(parsed, current_run):
    for element in parsed['current_hp_per_floor']:
        current_run.add_current_hp_for_floor(element)
    return current_run


def event_choices(parsed, current_run):
    if 'event_choices' in parsed:
        for element in parsed['event_choices']:
            run_event_choices = EventChoices()

            run_event_choices.add_damage_taken(element.get('damage_taken'))
            run_event_choices.add_event_name(element.get('event_name'))
            run_event_choices.add_floor(element.get('floor'))
            run_event_choices.add_player_choice(element.get('player_choice'))
            current_run.add_event_choices(run_event_choices)

    return current_run


def damage_taken(parsed, current_run):
    if 'damage_taken' in parsed:
        for element in parsed['damage_taken']:
            run_damage_taken = DamageTaken()

            run_damage_taken.add_damage(element.get('damage'))
            run_damage_taken.add_enemies(element.get('enemies'))
            run_damage_taken.add_floor(element.get('floor'))
            run_damage_taken.add_turns(element.get('turns'))

            current_run.add_damage_taken(run_damage_taken)
    return current_run


def gold_per_floor_all(parsed, current_run):
    for gold in parsed['gold_per_floor']:
        current_run.add_gold_for_floor(gold)
    return current_run


def items_purchased_all(parsed, current_run):
    for items in parsed['items_purchased']:
        current_run.add_items_purchased(items)
    return current_run


def master_deck_all(parsed, current_run):
    for card in parsed['master_deck']:
        current_run.add_master_deck(card)
    current_run.sort_master_deck()
    return current_run


def max_hp_per_floor_all(parsed, current_run):
    for max_hp in parsed['max_hp_per_floor']:
        current_run.add_max_hp_per_floor(max_hp)
    return current_run


def path_per_floor(parsed, current_run):
    for path in parsed['path_per_floor']:
        current_run.add_path_per_floor(path)
    return current_run


def path_taken(parsed, current_run):
    for taken in parsed['path_taken']:
        current_run.add_path_taken(taken)
    return current_run


def potions_floor_spawned(parsed, current_run):
    for potion in parsed['potions_floor_spawned']:
        current_run.add_potions_floor_spawned(potion)
    return current_run


def potions_floor_usage(parsed, current_run):
    for potion in parsed['potions_floor_usage']:
        current_run.add_potions_floor_usage(potion)
    return current_run


def potions_obtained(parsed, current_run):
    if 'potions_obtained' in parsed:
        for element in parsed['potions_obtained']:
            run_potions_obtained = PotionsObtained()

            run_potions_obtained.add_floor(element.get('floor'))
            run_potions_obtained.add_key(element.get('key'))
            current_run.add_potions_obtained(run_potions_obtained)

    return current_run


def relics(parsed, current_run):
    for relic in parsed['relics']:
        current_run.add_relics(relic)
    return current_run


# TODO: Refactor to store the value in the sts_run_data as a dict rather than a 'relics_obtained' object
def relics_obtained(parsed, current_run):
    if 'relics_obtained' in parsed:
        for element in parsed['relics_obtained']:
            run_relics_obtained = RelicsObtained()

            run_relics_obtained.add_floor(element.get('floor'))
            run_relics_obtained.add_key(element.get('key'))
            current_run.add_relics_obtained(run_relics_obtained)

    return current_run
