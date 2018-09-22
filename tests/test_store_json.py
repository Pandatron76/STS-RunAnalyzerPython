import sys
import os
import json
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from sts_run_history_analyzer import store_json  # noqa
from tests import create_mock  # noqa


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
