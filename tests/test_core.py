"""Tests for azure-mist."""
from azure.core import run


def test_run():
    result = run()
    assert result.ok
