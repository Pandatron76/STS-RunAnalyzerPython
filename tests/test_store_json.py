import sys
import os
import json
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from sts_run_history_analyzer import store_json  # noqa
from tests import create_mock  # noqa


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
