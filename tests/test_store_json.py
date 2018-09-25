import sys
import os
import json
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from sts_run_history_analyzer import store_json  # noqa
from tests import create_mock  # noqa


def test_card_choices():

    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_card_choices = json.loads(
        '{"card_choices":[{"not_picked":["Body Slam","Cleave"],"picked":"Uppercut","floor":1},'
        '{"not_picked":["Iron Wave","Bloodletting"],"picked":"Pommel Strike","floor":2},'
        '{"not_picked":["Twin Strike","Thunderclap"],"picked":"Iron Wave","floor":4},'
        '{"not_picked":["Havoc","Thunderclap","Iron Wave"],"picked":"SKIP","floor":10},'
        '{"not_picked":["Perfected Strike","Flex","Fire Breathing"],"picked":"SKIP","floor":12}]}'
    )

    store_json.card_choices(mock_card_choices, mock_run)

    assert mock_run.card_choices[0].floor == 1
    assert mock_run.card_choices[0].picked == "Uppercut"
    assert ["Body Slam", "Cleave"] == mock_run.card_choices[0].not_picked

    assert mock_run.card_choices[1].floor == 2
    assert mock_run.card_choices[1].picked == "Pommel Strike"
    assert ["Iron Wave", "Bloodletting"] == mock_run.card_choices[1].not_picked

    assert mock_run.card_choices[2].floor == 4
    assert mock_run.card_choices[2].picked == "Iron Wave"
    assert ["Twin Strike", "Thunderclap"] == mock_run.card_choices[2].not_picked

    assert mock_run.card_choices[3].floor == 10
    assert mock_run.card_choices[3].picked == "SKIP"
    assert ["Havoc", "Thunderclap", "Iron Wave"] == mock_run.card_choices[3].not_picked

    assert mock_run.card_choices[4].floor == 12
    assert mock_run.card_choices[4].picked == "SKIP"
    assert ["Perfected Strike", "Flex", "Fire Breathing"] == mock_run.card_choices[4].not_picked


def test_campfire_choices():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_campfire_choice = json.loads(
        '{"campfire_choices":[{"data":"True Grit","floor":6.0,"key":"SMITH"},'
        '{"floor":8.0,"key":"REST"},'
        '{"data":"Bash","floor":10.0,"key":"SMITH"},'
        '{"data":"Pommel Strike","floor":12.0,"key":"SMITH"},'
        '{"data":"Feel No Pain","floor":15.0,"key":"SMITH"}]}'
    )

    store_json.campfire_choice(mock_campfire_choice, mock_run)

    assert mock_run.campfire_choices[0].floor == 6.0
    assert mock_run.campfire_choices[0].key == "SMITH"
    assert mock_run.campfire_choices[0].data == "True Grit"

    assert mock_run.campfire_choices[1].floor == 8.0
    assert mock_run.campfire_choices[1].key == "REST"

    assert mock_run.campfire_choices[2].floor == 10.0
    assert mock_run.campfire_choices[2].key == "SMITH"
    assert mock_run.campfire_choices[2].data == "Bash"

    assert mock_run.campfire_choices[3].floor == 12.0
    assert mock_run.campfire_choices[3].key == "SMITH"
    assert mock_run.campfire_choices[3].data == "Pommel Strike"

    assert mock_run.campfire_choices[4].floor == 15.0
    assert mock_run.campfire_choices[4].key == "SMITH"
    assert mock_run.campfire_choices[4].data == "Feel No Pain"


def test_current_hp_per_floor():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_current_hp_per_floor = json.loads('{"current_hp_per_floor":[32,30,36,36,22,46,46,46,46,39,39,35,32,32,56,0]}')

    store_json.current_hp_per_floor(mock_current_hp_per_floor, mock_run)

    assert 32 in mock_run.current_hp_per_floor
    assert 30 in mock_run.current_hp_per_floor
    assert 36 in mock_run.current_hp_per_floor
    assert 22 in mock_run.current_hp_per_floor
    assert 46 in mock_run.current_hp_per_floor
    assert 39 in mock_run.current_hp_per_floor
    assert 35 in mock_run.current_hp_per_floor
    assert 32 in mock_run.current_hp_per_floor
    assert 56 in mock_run.current_hp_per_floor
    assert 0 in mock_run.current_hp_per_floor


def test_event_choices():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_event_choices = json.loads(
        '{"event_choices":[{"event_name":"Liars Game","player_choice":"disagreed","floor":3.0,"damage_taken":0.0},'
        '{"event_name":"Scrap Ooze","player_choice":"success","floor":4.0,"damage_taken":7.0},'
        '{"event_name":"The Joust","player_choice":"Bet on Murderer","floor":19.0,"damage_taken":0.0},'
        '{"event_name":"Vampires","player_choice":"Became a vampire","floor":30.0,"damage_taken":0.0},'
        '{"event_name":"WeMeetAgain","player_choice":"Card","floor":31.0,"damage_taken":0.0}]}'
    )

    store_json.event_choices(mock_event_choices, mock_run)

    assert mock_run.event_choices[0].event_name == "Liars Game"
    assert mock_run.event_choices[0].player_choice == "disagreed"
    assert mock_run.event_choices[0].floor == 3.0
    assert mock_run.event_choices[0].damage_taken == 0.0

    assert mock_run.event_choices[1].event_name == "Scrap Ooze"
    assert mock_run.event_choices[1].player_choice == "success"
    assert mock_run.event_choices[1].floor == 4.0
    assert mock_run.event_choices[1].damage_taken == 7.0

    assert mock_run.event_choices[2].event_name == "The Joust"
    assert mock_run.event_choices[2].player_choice == "Bet on Murderer"
    assert mock_run.event_choices[2].floor == 19.0
    assert mock_run.event_choices[2].damage_taken == 0.0

    assert mock_run.event_choices[3].event_name == "Vampires"
    assert mock_run.event_choices[3].player_choice == "Became a vampire"
    assert mock_run.event_choices[3].floor == 30.0
    assert mock_run.event_choices[3].damage_taken == 0.0

    assert mock_run.event_choices[4].event_name == "WeMeetAgain"
    assert mock_run.event_choices[4].player_choice == "Card"
    assert mock_run.event_choices[4].floor == 31.0
    assert mock_run.event_choices[4].damage_taken == 0.0


def test_damage_taken():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_damage_taken = json.loads(
        '{"damage_taken":[{"damage":10,"enemies":"Cultist","floor":1,"turns":5},'
        '{"damage":8,"enemies":"Jaw Worm","floor":2,"turns":5},'
        '{"damage":0,"enemies":"2 Louse","floor":3,"turns":4}]}')

    store_json.damage_taken(mock_damage_taken, mock_run)

    assert mock_run.damage_taken[0].damage == 10
    assert mock_run.damage_taken[0].enemies == "Cultist"
    assert mock_run.damage_taken[0].floor == 1
    assert mock_run.damage_taken[0].turns == 5

    assert mock_run.damage_taken[1].damage == 8
    assert mock_run.damage_taken[1].enemies == "Jaw Worm"
    assert mock_run.damage_taken[1].floor == 2
    assert mock_run.damage_taken[1].turns == 5

    assert mock_run.damage_taken[2].damage == 0
    assert mock_run.damage_taken[2].enemies == "2 Louse"
    assert mock_run.damage_taken[2].floor == 3
    assert mock_run.damage_taken[2].turns == 4


def test_gold_per_floor_all():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_gold_per_floor_all = json.loads(
        '{"gold_per_floor":[111, 126, 3, 18, 18, 18, 18, 18, 18, 53, 53, 80, 30, 41, 41, '
        '143, 143, 159, 170, 180, 196, 121, 121, 176, 187, 213, 231, 231, 246, 246, '
        '273, 273, 373, 373, 387, 397, 40, 54, 54]}'
    )

    store_json.gold_per_floor_all(mock_gold_per_floor_all, mock_run)

    assert 111 in mock_run.gold_per_floor
    assert 18 in mock_run.gold_per_floor
    assert 3 in mock_run.gold_per_floor
    assert 0 not in mock_run.gold_per_floor
    assert -1 not in mock_run.gold_per_floor


def test_items_purchased_all():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_items_purchased_all = json.loads(
        '{"items_purchased":["Metallicize",'
        '"Armaments",'
        '"Bottled Lightning",'
        '"Metallicize",'
        '"Energy Potion"]}'
    )

    store_json.items_purchased_all(mock_items_purchased_all, mock_run)

    assert "Metallicize" in mock_run.items_purchased
    assert "Armaments" in mock_run.items_purchased
    assert "Bottled Lightning" in mock_run.items_purchased
    assert "Energy Potion" in mock_run.items_purchased


def test_master_deck_all():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_master_deck_all = json.loads(
        '{"master_deck":["Strike_R+1","Strike_R","Strike_R","Strike_R","Defend_R",'
        '"Defend_R+1","Defend_R+1","Defend_R+1","Bash","Whirlwind",'
        '"Anger","Headbutt","Rampage","Metallicize","Pommel Strike"]}'
    )

    store_json.master_deck_all(mock_master_deck_all, mock_run)

    assert "Strike_R+1" in mock_run.master_deck
    assert "Strike_R" in mock_run.master_deck
    assert "Defend_R" in mock_run.master_deck
    assert "Defend_R+1" in mock_run.master_deck
    assert "Bash" in mock_run.master_deck
    assert "Whirlwind" in mock_run.master_deck
    assert "Anger" in mock_run.master_deck
    assert "Headbutt" in mock_run.master_deck
    assert "Rampage" in mock_run.master_deck
    assert "Metallicize" in mock_run.master_deck
    assert "Pommel Strike" in mock_run.master_deck


def test_max_hp_per_floor_all():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_max_hp_per_floor_all = json.loads(
        '{"max_hp_per_floor":[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,'
        '88,88,92,96,96,100,104,108,108,108,108,108,112,112,116,'
        '116,116,116,116,120,120,120,120,124,124,124,124,124,124,128,128,128,132,132,132]}'
    )

    store_json.max_hp_per_floor_all(mock_max_hp_per_floor_all, mock_run)

    assert 88 in mock_run.max_hp_per_floor
    assert 92 in mock_run.max_hp_per_floor
    assert 96 in mock_run.max_hp_per_floor
    assert 100 in mock_run.max_hp_per_floor
    assert 104 in mock_run.max_hp_per_floor
    assert 108 in mock_run.max_hp_per_floor
    assert 112 in mock_run.max_hp_per_floor
    assert 116 in mock_run.max_hp_per_floor
    assert 120 in mock_run.max_hp_per_floor
    assert 124 in mock_run.max_hp_per_floor
    assert 128 in mock_run.max_hp_per_floor
    assert 132 in mock_run.max_hp_per_floor


def test_path_per_floor():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_path_per_floor = json.loads(
        '{"path_per_floor":["M","?","M","?","?","R","E","M","T","M","?","R","T","M","R","B",'
        'null,"M","M","M","?","$","R","?","R","T","?","?","E","$","M","R","B",'
        'null,"M","M","?","M","?","R","M","T","T","M","?","$","M","M","R","B"]}'
    )

    store_json.path_per_floor(mock_path_per_floor, mock_run)

    assert "M" in mock_run.path_per_floor
    assert "?" in mock_run.path_per_floor
    assert "R" in mock_run.path_per_floor
    assert "E" in mock_run.path_per_floor
    assert "T" in mock_run.path_per_floor
    assert "B" in mock_run.path_per_floor
    assert None in mock_run.path_per_floor


def test_path_taken():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_path_taken = json.loads(
        '{"path_taken":["M","?","M","?","?","R","E","M","T","?","?","R","?","M","R","BOSS",'
        '"M","M","M","?","$","R","?","R","T","?","?","E","$","M","R","BOSS",'
        '"M","M","?","M","?","R","M","?","T","?","?","?","M","M","R","BOSS"]}'
    )

    store_json.path_taken(mock_path_taken, mock_run)

    assert "M" in mock_run.path_taken
    assert "?" in mock_run.path_taken
    assert "$" in mock_run.path_taken
    assert "E" in mock_run.path_taken
    assert "R" in mock_run.path_taken
    assert "BOSS" in mock_run.path_taken


def test_potions_floor_spawned():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_potions_floor_spawned = json.loads('{"potions_floor_spawned":[3,7,14,18,31,35,38,47]}')

    store_json.potions_floor_spawned(mock_potions_floor_spawned, mock_run)

    assert mock_run.potions_floor_spawned[0] == 3
    assert mock_run.potions_floor_spawned[1] == 7
    assert mock_run.potions_floor_spawned[2] == 14
    assert mock_run.potions_floor_spawned[3] == 18
    assert mock_run.potions_floor_spawned[4] == 31
    assert mock_run.potions_floor_spawned[5] == 35
    assert mock_run.potions_floor_spawned[6] == 38
    assert mock_run.potions_floor_spawned[7] == 47


def test_potions_floor_usage():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_potions_floor_usage = json.loads('{"potions_floor_usage":[7,16,29,33,33,33,44,48,50]}')

    store_json.potions_floor_usage(mock_potions_floor_usage, mock_run)

    assert mock_run.potions_floor_usage[0] == 7
    assert mock_run.potions_floor_usage[1] == 16
    assert mock_run.potions_floor_usage[2] == 29
    assert mock_run.potions_floor_usage[3] == 33
    assert mock_run.potions_floor_usage[4] == 33
    assert mock_run.potions_floor_usage[5] == 33
    assert mock_run.potions_floor_usage[6] == 44
    assert mock_run.potions_floor_usage[7] == 48
    assert mock_run.potions_floor_usage[8] == 50


def test_potions_obtained():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_potions_obtained = json.loads(
        '{"potions_obtained":[{"floor":3,"key":"Block Potion"},'
        '{"floor":7,"key":"AttackPotion"},'
        '{"floor":14,"key":"LiquidBronze"},'
        '{"floor":18,"key":"Weak Potion"},'
        '{"floor":31,"key":"EntropicBrew"}]}')

    store_json.potions_obtained(mock_potions_obtained, mock_run)

    assert mock_run.potions_obtained[0].floor == 3
    assert mock_run.potions_obtained[0].key == "Block Potion"

    assert mock_run.potions_obtained[1].floor == 7
    assert mock_run.potions_obtained[1].key == "AttackPotion"

    assert mock_run.potions_obtained[2].floor == 14
    assert mock_run.potions_obtained[2].key == "LiquidBronze"

    assert mock_run.potions_obtained[3].floor == 18
    assert mock_run.potions_obtained[3].key == "Weak Potion"

    assert mock_run.potions_obtained[4].floor == 31
    assert mock_run.potions_obtained[4].key == "EntropicBrew"


def test_relic():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_relics = json.loads(
        '{"relics":["Burning Blood",'
        '"Red Skull",'
        '"Paper Phrog",'
        '"Champion Belt",'
        '"Mark of Pain"]}')

    store_json.relics(mock_relics, mock_run)
    assert "Burning Blood" in mock_run.relics
    assert "Red Skull" in mock_run.relics
    assert "Paper Phrog" in mock_run.relics
    assert "Champion Belt" in mock_run.relics
    assert "Mark of Pain" in mock_run.relics


def test_relic_obtained():
    mock_run = create_mock.sts_run_data('0123456789.run')
    mock_obtained_relics = json.loads(
        '{"relics_obtained":[{"floor":7,"key":"Red Skull"},'
        '{"floor":9,"key":"Paper Phrog"},'
        '{"floor":13,"key":"Champion Belt"},'
        '{"floor":21,"key":"Mark of Pain"}]}')

    store_json.relics_obtained(mock_obtained_relics, mock_run)

    assert mock_run.relics_obtained[0].floor == 7
    assert mock_run.relics_obtained[0].key == "Red Skull"

    assert mock_run.relics_obtained[1].floor == 9
    assert mock_run.relics_obtained[1].key == "Paper Phrog"

    assert mock_run.relics_obtained[2].floor == 13
    assert mock_run.relics_obtained[2].key == "Champion Belt"

    assert mock_run.relics_obtained[3].floor == 21
    assert mock_run.relics_obtained[3].key == "Mark of Pain"
