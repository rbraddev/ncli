import pytest
from typer.testing import CliRunner

from cli.main import app

runner = CliRunner()


@pytest.fixture(scope="function")
def cli_result(request):
    marker = request.node.get_closest_marker("command")
    return runner.invoke(app, marker.args[0])
