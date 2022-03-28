import pytest


@pytest.mark.command(["find", "mac", "da08", "--username", "user", "--password", "pass"])
def test_mac(cli_result):
    assert "DA-08" in cli_result.stdout
