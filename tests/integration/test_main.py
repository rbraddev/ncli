import pytest

from cli.utils.version import get_version


@pytest.mark.command("--version")
def test_version(cli_result):
    version = get_version()
    assert f"ncli version: {version}" in cli_result.stdout
