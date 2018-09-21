import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../sts_run_history_analyzer"))

from tests import create_mock  # noqa


def test_current_run():
    mock_run = create_mock.sts_run_data('0123456789.run')
    assert mock_run.starting_gold == 99