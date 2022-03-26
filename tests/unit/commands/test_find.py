import pytest
from typer import BadParameter

from cli.commands.find import validate_mac


@pytest.mark.parametrize("input_mac, expected_mac", [("a1b2", "a1-b2"), ("a1b2c3d4e5f6", "a1-b2-c3-d4-e5-f6")])
def test_validate_mac_success(input_mac, expected_mac):
    mac = validate_mac(input_mac)

    assert mac == expected_mac


@pytest.mark.parametrize(
    "input_mac, error_msg",
    [
        ("a1a1a1", "Please enter the full or last 4 characters of the MAC address"),
        ("bogusmac1234", "Invalid MAC: bogusmac1234"),
    ],
)
def test_validate_mac_fail(input_mac, error_msg):
    with pytest.raises(BadParameter, match=error_msg):
        validate_mac(input_mac)
