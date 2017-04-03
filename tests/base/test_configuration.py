import pytest
import os

from src.base.configuration import Configuration


@pytest.fixture(scope="function", autouse=True)
def configuration():
    return Configuration(os.path.dirname(os.path.realpath(__file__)) + '/../test_config.ini')


def test_default_values(configuration):
    assert configuration.REDIS.port == '40001'
    assert configuration.REDIS.server == '127.0.0.1'
    assert configuration.REDIS.password == 'crosswalks'
    assert configuration.DETECTION.word == 'crosswalk'
    assert configuration.DETECTION.compare == 'yes'
    assert configuration.DETECTION.barrier == '0.99'
    assert configuration.DETECTION.followstreets == 'yes'
    assert configuration.JOB.timeout == '5400'
    assert configuration.JOB.bboxsize == '2000'
