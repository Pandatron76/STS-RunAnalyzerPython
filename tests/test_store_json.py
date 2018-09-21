import sys
import os
import json
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from sts_run_history_analyzer import store_json  # noqa
from tests import create_mock  # noqa


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
