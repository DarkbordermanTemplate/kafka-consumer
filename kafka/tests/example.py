"""Tests for example topic handler"""
from topics.example import EXAMPLE_HANDLER

INPUT = b"Example text"

OUTPUT = b"Example text"


def test_example_topic():
    """Test for ensuring example handler works as expected"""

    assert EXAMPLE_HANDLER.topic == "example"
    assert EXAMPLE_HANDLER.handle(INPUT) == OUTPUT
