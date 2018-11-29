import sys
import os
import json

from config import check_config, config_helper

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from tests import create_mock  # noqa


def test_check_config_item_values():
    mock_config = create_mock.all_true_config()
    mock_run = create_mock.sts_run_data('0123456789.run_data')
    mock_json = json.loads(create_mock.sample_raw_json())
    mock_config_items = check_config.print_single_run(mock_config, mock_run, mock_json)

    assert list == type(mock_config_items)
    # assert 28 == len(mock_config_items)


def test_target_path():
    mock_config = create_mock.all_false_config()
    assert config_helper.read_target_path(mock_config) == ''


def test_section_to_bool_dict():
    mock_config = create_mock.all_false_config()
    assert type(config_helper.section_to_bool_dict(mock_config, 'PRINT_ALL_RUNS')) is dict
    assert type(config_helper.section_to_bool_dict(mock_config, 'FAKE_SECTION')) is dict


def test_string_to_bool():
    assert config_helper.string_to_bool('True') is True
    assert config_helper.string_to_bool('False') is False
    assert config_helper.string_to_bool('foo') is None
    assert config_helper.string_to_bool(0) is None
    assert config_helper.string_to_bool(-1) is None
    assert config_helper.string_to_bool(1) is None
