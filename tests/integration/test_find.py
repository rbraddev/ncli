import pytest


@pytest.mark.command(["find", "mac", "8b85", "--username", "user", "--password", "pass"])
def test_mac(cli_result):
    assert "8B-85" in cli_result.stdout
