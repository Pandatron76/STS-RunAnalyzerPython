from report import report_summary
from run_data import campfire
from individual_runs import store_run_lists


def store_console_messages(current_run, parsed, config_item_print_individual):
    for config_item in config_item_print_individual:
        if 'BuildVersion' == config_item.config_item_name:
            current_run.build_version = parsed.get('build_version')
            config_item.console_message = "Build Version: %s" % current_run.build_version

        if 'Timestamp' == config_item.config_item_name:
            current_run.timestamp = parsed.get('timestamp')
            config_item.console_message = "Timestamp: %s" % current_run.timestamp

        if 'SpecialSeed' == config_item.config_item_name:
            current_run.special_seed = parsed.get('special_seed')
            config_item.console_message = "Special Seed: %s" % current_run.special_seed

        # TODO Include section_dict check for overview
        if 'OverviewIndividual' == config_item.config_item_name:
            config_item.console_message += report_summary.create_title_header("General Stats:")

            # Store the overview information
            current_run.character_chosen = parsed.get('character_chosen')
            current_run.ascension = parsed.get('ascension_level')
            current_run.victory = parsed.get('victory')
            current_run.floor_reached = parsed.get('floor_reached')
            current_run.campfire_rested = parsed.get('campfire_rested')
            current_run.campfire_upgraded = parsed.get('campfire_upgraded')
            # TODO Remove Total Gold Gained and Total Gold Spent/Lost for now.
            # TODO Remove Boss relic info for now

            config_item.console_message += "  Character chosen: %s\n" % current_run.character_chosen
            config_item.console_message += "  Ascension %s\n" % current_run.ascension
            config_item.console_message += "  Victory %s" % current_run.victory
            config_item.console_message += "  Floor reached: %s\n" % current_run.floor_reached
            config_item.console_message += "  Campfire rested: %s\n" % current_run.campfire_rested
            config_item.console_message += "  Campfire upgraded: %s\n" % current_run.campfire_upgraded

        if 'CharacterChosen' == config_item.config_item_name:
            current_run.character_chosen = parsed.get('character_chosen')
            config_item.console_message = "Character Chosen: %s" % current_run.character_chosen

        if 'Ascension' == config_item.config_item_name:
            current_run.ascension = parsed.get('ascension_level')
            config_item.console_message = "Ascension: %s" % current_run.ascension

        if 'Victory' == config_item.config_item_name:
            current_run.victory = parsed.get('victory')
            config_item.console_message = "Victory: %s" % current_run.victory

        if 'WinRate' == config_item.config_item_name:
            current_run.win_rate = parsed.get('win_rate')
            config_item.console_message = "Win Rate: %s" % current_run.win_rate

        if 'FloorReached' == config_item.config_item_name:
            current_run.floor_reached = parsed.get('floor_reached')
            config_item.console_message = "Floor Reached: %s" % current_run.floor_reached

        if 'Score' == config_item.config_item_name:
            current_run.score = parsed.get('score')
            config_item.console_message = "Score: %s" % current_run.score

        if 'NeowBonus' == config_item.config_item_name:
            current_run.neow_bonus = parsed.get('neow_bonus')
            config_item.console_message = "Neow Bonus: %s" % current_run.neow_bonus

        if 'NeowCost' == config_item.config_item_name:
            current_run.neow_cost = parsed.get('neow_cost')
            config_item.console_message = "Neow Cost: %s" % current_run.neow_cost

        if 'CampfireRested' == config_item.config_item_name:
            current_run.campfire_rested = parsed.get('campfire_rested')
            config_item.console_message = "Campfire Rested: %s" % current_run.campfire_rested

        if 'CampfireUpgraded' == config_item.config_item_name:
            current_run.campfire_upgraded = parsed.get('campfire_upgraded')
            config_item.console_message = "Campfire Upgraded: %s" % current_run.campfire_upgraded

        if 'ChosenSeed' == config_item.config_item_name:
            current_run.chosen_seed = parsed.get('chose_seed')
            config_item.console_message = "Chosen Seed: %s" % current_run.chosen_seed

        if 'CircletCount' == config_item.config_item_name:
            current_run.circlet_count = parsed.get('circlet_count')
            config_item.console_message = "Circlet Count: %s" % current_run.circlet_count

        if 'Gold' == config_item.config_item_name:
            current_run.gold = parsed.get('gold')
            config_item.console_message = "Gold: %s" % current_run.gold

        if 'IsAscensionMode' == config_item.config_item_name:
            current_run.is_ascension_mode = parsed.get('is_ascension_mode')
            config_item.console_message = "Is Ascension Mode: %s" % current_run.is_ascension_mode

        if 'IsDaily' == config_item.config_item_name:
            current_run.is_daily = parsed.get('is_daily')
            config_item.console_message = "Is Daily: %s" % current_run.is_daily

        if 'IsEndless' == config_item.config_item_name:
            current_run.is_endless = parsed.get('is_endless')
            config_item.console_message = "Is Endless: %s" % current_run.is_endless

        if 'IsProd' == config_item.config_item_name:
            current_run.is_prod = parsed.get('is_prod')
            config_item.console_message = "Is Prod: %s" % current_run.is_prod

        if 'IsTrial' == config_item.config_item_name:
            current_run.is_trial = parsed.get('is_trial')
            config_item.console_message = "Is Trial: %s" % current_run.is_trial

        if 'PlayId' == config_item.config_item_name:
            current_run.play_id = parsed.get('play_id')
            config_item.console_message = "Play Id: %s" % current_run.play_id

        if 'PlayerExperience' == config_item.config_item_name:
            current_run.player_experience = parsed.get('player_experience')
            config_item.console_message = "Player Experience: %s" % current_run.player_experience

        if 'Playtime' == config_item.config_item_name:
            current_run.playtime = parsed.get('playtime')
            config_item.console_message = "Playtime: %s" % current_run.playtime

        if 'PurchasedPurges' == config_item.config_item_name:
            current_run.purchased_purges = parsed.get('purchased_purges')
            config_item.console_message = "Purchased Purges: %s" % current_run.purchased_purges

        if 'SeedSourceTimestamp' == config_item.config_item_name:
            current_run.seed_source_timestamp = parsed.get('seed_source_timestamp')
            config_item.console_message = "Seed Source Timestamp: %s" % current_run.seed_source_timestamp

        if 'BossRelicPickedActOne' == config_item.config_item_name:
            config_item.console_message += \
                "    Boss Relic picked Act One: %s" % current_run.boss_relic_picked_act1

        if 'BossRelicNotPickedActOne' == config_item.config_item_name:
            config_item.console_message += \
                "    Boss Relic not picked Act One: %s" % current_run.boss_relic_not_picked_act1

        if 'BossRelicPickedActTwo' == config_item.config_item_name:
            config_item.console_message += \
                "    Boss Relic picked Act Two: %s" % current_run.boss_relic_picked_act2

        if 'BossRelicNotPickedActTwo' == config_item.config_item_name:
            config_item.console_message += \
                "    Boss Relic not picked Act Two: %s" % current_run.boss_relic_not_picked_act2

        if 'CampfireChoices' == config_item.config_item_name:
            console_message = "Campfire Choices:\n"

            campfire.store_campfire_choices(current_run, parsed)

            if current_run.campfire_choices:
                for choice in current_run.campfire_choices:
                    if choice.data:
                        console_message += "    Floor: %s || Action: %s || Data: %s\n" % \
                                           (choice.floor, choice.key, choice.data)
                    else:
                        console_message += "    Floor: %s || Action: %s\n" % (choice.floor, choice.key)

            config_item.console_message = console_message

        if 'CardChoices' == config_item.config_item_name:
            console_message = "Card Choices\n"

            store_run_lists.card_choices(current_run, parsed)

            for card in current_run.card_choices:
                console_message += "    Floor: %s || Picked: %s || Not Picked: %s\n" % \
                                   (card.floor, card.picked, card.not_picked)

            config_item.console_message = console_message

        if 'CurrentHpPerFloor' == config_item.config_item_name:
            console_message = "Current HP per Floor:\n"
            floor_count = 0

            store_run_lists.current_hp_per_floor(current_run, parsed)

            # Store the console message to display to the end user
            for current_hp in current_run.current_hp_per_floor:
                if floor_count <= len(parsed['current_hp_per_floor']):
                    console_message += "    Floor: %s || Current HP: %s\n" % (floor_count, current_hp)
                    floor_count += 1
                else:
                    console_message += "    Floor: %s || Current HP: %s" % (floor_count, current_hp)

            config_item.console_message = console_message

        if 'DamageTaken' == config_item.config_item_name:
            console_message = "Damage Taken:\n"
            store_run_lists.damage_taken(current_run, parsed)

            # Store the console message to display to the end user
            for x in current_run.damage_taken:
                console_message += "  Floor: %s\n" % x.floor
                console_message += "    Enemies: %s\n" % x.enemies
                console_message += "    Turns: %s\n" % x.turns
                console_message += "    Damage: %s\n" % x.damage

            config_item.console_message = console_message

        if 'EventChoices' == config_item.config_item_name:
            console_message = "Event Choices:"
            store_run_lists.event_choices(current_run, parsed)

            for x in current_run.event_choices:
                console_message += "  Floor: %s\n" % x.floor
                console_message += "    Event Name: %s\n" % x.event_name
                console_message += "      Player Choice: %s\n" % x.player_choice
                console_message += "      Damage Taken: %s\n" % x.damage_taken

            config_item.console_message = console_message

        # TODO: Reduce complexity of GoldPerFloor (it is doing more than it should)
        if 'GoldPerFloor' == config_item.config_item_name:
            console_message = "Gold per Floor:\n"
            indent = '  '
            new_line = '\n'
            double_indent = indent + indent
            floor_number = 1
            previous_gold_value = 0
            total_gold_gained = 0
            total_gold_lost = 0

            store_run_lists.gold_per_floor_all(current_run, parsed)

            # Check to see if 'gold_per_floor' is present in parsed (json)
            if 'gold_per_floor' in parsed:
                # Check each value in the 'gold_per_floor' array
                for element in parsed['gold_per_floor']:
                    current_floor = "%sFloor: %s" % (double_indent, floor_number)
                    current_gold = "%sGold: %s" % (double_indent, element)

                    # Display current floor and how much gold they have (example: "Floor: 27 \n  Gold: 127)
                    console_message += current_floor + new_line + indent + current_gold

                    # The first floor is the exception as the user could start with...
                    # 0 (neow_cost), 99 or 199 gold (neow_bonus)
                    if floor_number == 1:
                        # This assumes the user has the starting gold or more than their starting gold (neow_bonus)
                        if element > current_run.starting_gold:
                            console_message += "%s%s%sDiff: +%s\n" % \
                                               (new_line, double_indent, indent,
                                                str(element - current_run.starting_gold))

                            total_gold_gained += element - current_run.starting_gold
                            current_run.add_gold_for_floor(element - current_run.starting_gold)

                        # This assumes the user gave neow all their gold (neow_cost)
                        else:
                            console_message += "%s%s%sDiff: +%s\n" % \
                                               (new_line, double_indent, indent, str(element))
                            total_gold_gained += element
                            current_run.add_gold_for_floor(element)

                    # For every other floor...
                    elif floor_number != 1:
                        # User did not gain or lose any gold (Example: Skipped Shop, No Cost Event, Ectoplasm relic)
                        if element - previous_gold_value == 0:
                            console_message += '%s(No Change)\n' % indent
                        # User gained gold, spent or used their gold for an event
                        elif element - previous_gold_value != 0:
                            # The user gained gold, update total_gold_gained
                            if element - previous_gold_value > 0:
                                console_message += "%s%s%sDiff: +%s\n" % \
                                                   (new_line, double_indent, indent,
                                                    str(element - previous_gold_value))
                                total_gold_gained += element - previous_gold_value
                            # The user spent/lost gold, update total_gold_lost
                            else:
                                console_message += "%s%s%sDiff: %s\n" % \
                                                   (new_line, double_indent, indent,
                                                    str(element - previous_gold_value))
                                total_gold_lost += element - previous_gold_value

                    else:
                        print('Unexpected result... with printing gold_per_floor_all')

                    previous_gold_value = element

                    current_run.add_gold_for_floor(element)
                    current_run.add_total_gold_gained(total_gold_gained)
                    current_run.add_total_gold_lost(total_gold_lost)

                    console_message += "%s %s Total Gained: +%s\n" % (double_indent, indent, total_gold_gained)
                    console_message += "%s %s Total Spent/Lost: %s\n" % (double_indent, indent, total_gold_lost)
                    floor_number += 1

            config_item.console_message = console_message

        if 'ItemsPurchased' == config_item.config_item_name:
            console_message = "Items Purchased:\n"
            store_run_lists.items_purchased_all(current_run, parsed)

            for item_purchased in current_run.items_purchased:
                console_message += "    %s\n" % item_purchased

            config_item.console_message = console_message

        if 'MasterDeck' == config_item.config_item_name:
            console_message = "Master Deck (Ordered by: acquisition):\n"
            store_run_lists.master_deck_all(current_run, parsed)

            for card_in_deck in current_run.master_deck:
                console_message += "    %s\n" % card_in_deck

            config_item.console_message = console_message

        if 'MaxHpPerFloor' == config_item.config_item_name:
            console_message = "Max HP per Floor:\n"
            floor_count = 0
            store_run_lists.max_hp_per_floor_all(current_run, parsed)

            for max_hp in current_run.max_hp_per_floor:
                console_message += "    Floor: %s || Max HP: %s\n" % (floor_count, max_hp)
                floor_count += 1

            config_item.console_message = console_message

        if 'PathPerFloor' == config_item.config_item_name:
            console_message = "Path Per Floor:\n"
            floor_count = 0
            store_run_lists.path_per_floor(current_run, parsed)

            for path in current_run.path_per_floor:
                console_message += "    Floor: %s || Letter: %s\n" % (floor_count, path)
                floor_count += 1

            config_item.console_message = console_message

        if 'PathTakenPerFloor' == config_item.config_item_name:
            console_message = "Path Taken:\n"
            store_run_lists.path_taken(current_run, parsed)

            for path_taken in current_run.path_taken:
                console_message += "    %s\n" % path_taken

            config_item.console_message = console_message

        if 'PotionsFloorSpawned' == config_item.config_item_name:
            console_message = "Potions Spawned per Floor:\n"
            store_run_lists.potions_floor_spawned(current_run, parsed)

            for potion in current_run.potions_floor_spawned:
                console_message += "    %s\n" % potion

            config_item.console_message = console_message

        if 'PotionsObtained' == config_item.config_item_name:
            console_message = "Potions Obtained Per Floor:\n"
            store_run_lists.potions_obtained(current_run, parsed)

            if 'potions_obtained' in parsed:
                for element in parsed['potions_obtained']:
                    console_message += "    Floor: %s || Potion: %s\n" % (element.get('floor'), element.get('key'))

            config_item.console_message = console_message

        if 'Relics' == config_item.config_item_name:
            console_message = "Relics:\n"
            store_run_lists.relics(current_run, parsed)

            for relic in parsed['relics']:
                console_message += "    %s\n" % relic

            config_item.console_message = console_message

        # TODO: Refactor to store the value in the sts_run_data as a dict rather than a 'relics_obtained' object
        if 'RelicsObtained' == config_item.config_item_name:
            console_message = "Relics Obtained:\n"
            store_run_lists.relics_obtained(current_run, parsed)

            if 'relics_obtained' in parsed:
                for element in parsed['relics_obtained']:
                    console_message += "    Floor: %s || Relic: %s\n" % (element.get('floor'), element.get('key'))

            config_item.console_message = console_message

        if 'SeedPlayed' == config_item.config_item_name:
            current_run.build_version = parsed.get('seed_played')
            config_item.console_message = "Seed Played: %s" % current_run.build_version

    return config_item_print_individual
