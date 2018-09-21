import sys
import os

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from sts_run_history_analyzer import config_helper  # noqa
from tests import create_mock  # noqa


def test_target_path():
    mock_config = create_mock.config()
    assert config_helper.read_target_path(mock_config) == ''


def test_section_to_bool_dict():
    mock_config = create_mock.config()
    assert type(config_helper.section_to_bool_dict(mock_config, 'PRINT_ALL_RUNS')) is dict
    assert type(config_helper.section_to_bool_dict(mock_config, 'FAKE_SECTION')) is dict


def test_string_to_bool():
    assert config_helper.string_to_bool('True') is True
    assert config_helper.string_to_bool('False') is False
    assert config_helper.string_to_bool('foo') is None
    assert config_helper.string_to_bool(0) is None
    assert config_helper.string_to_bool(-1) is None
    assert config_helper.string_to_bool(1) is None
