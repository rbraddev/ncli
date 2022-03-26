from unittest import mock

from cli.utils.version import get_version


def test_get_version(monkeypatch):
    def mockread():
        return """
            name = "ncli"
            version = "0.1.0"
            description = ""
        """

    mock.patch("TextIOWrapper.read", return_value=mockread())
    version = get_version()

    assert version == "0.1.0"
